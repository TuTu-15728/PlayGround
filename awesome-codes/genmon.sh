#!/bin/bash
# Simple system monitor for GenMon


# Get IP
get_network_ip() {
    # Check tun0 first (highest priority)
    if ip addr show tun0 &>/dev/null; then
        tun0_ip=$(ip addr show tun0 | grep -oP 'inet \K[\d.]+' | head -1)
        if [ -n "$tun0_ip" ]; then
            echo "$tun0_ip"
            return 0
        fi
    fi
    
    # Check wlo1 second
    if ip addr show wlo1 &>/dev/null; then
        wlo1_ip=$(ip addr show wlo1 | grep -oP 'inet \K[\d.]+' | head -1)
        if [ -n "$wlo1_ip" ]; then
            echo "$wlo1_ip"
            return 0
        fi
    fi
    
    # Check wlan1 third
    if ip addr show wlan1 &>/dev/null; then
        wlan1_ip=$(ip addr show wlan1 | grep -oP 'inet \K[\d.]+' | head -1)
        if [ -n "$wlan1_ip" ]; then
            echo "$wlan1_ip"
            return 0
        fi
    fi
    
    # Default if nothing found
    echo "127.0.0.1"
    return 1
}


# Get Battery
get_battery() {
    # Try multiple common battery paths
    for bat in /sys/class/power_supply/BAT*; do
        if [ -d "$bat" ]; then
            capacity=$(cat "$bat/capacity" 2>/dev/null)
            status=$(cat "$bat/status" 2>/dev/null)
            
            if [ -n "$capacity" ]; then
                case "$status" in
                    "Charging") echo "⚡ $capacity%" ;;
                    "Discharging") echo "⏳ $capacity%" ;;
                    "Full") echo "🛢 $capacity%" ;;
                    *) echo "?$capacity%" ;;
                esac
                return 0
            fi
        fi
    done
    
    # Fallback if no battery found
    echo "No BAT"
}

# Get Net Speed

get_download_speed() {
    # Determine which interface to monitor
    local interface=""
    if ip addr show wlo1 &>/dev/null && ip addr show wlo1 | grep -q "inet "; then
        interface="wlo1"
    elif ip addr show wlan1 &>/dev/null && ip addr show wlan1 | grep -q "inet "; then
        interface="wlan1"
    else
        echo "0B/s"
        return
    fi
    
    # Get initial RX bytes
    initial_rx=$(cat /sys/class/net/$interface/statistics/rx_bytes 2>/dev/null)
    sleep 1
    final_rx=$(cat /sys/class/net/$interface/statistics/rx_bytes 2>/dev/null)
    
    # Calculate speed
    if [ -n "$initial_rx" ] && [ -n "$final_rx" ]; then
        bytes_per_sec=$((final_rx - initial_rx))
        
        # Convert to human readable
        if [ $bytes_per_sec -ge 1048576 ]; then
            echo "$(echo "scale=1; $bytes_per_sec/1048576" | bc)MB/s"
        elif [ $bytes_per_sec -ge 1024 ]; then
            echo "$(echo "scale=1; $bytes_per_sec/1024" | bc)KB/s"
        else
            echo "${bytes_per_sec}B/s"
        fi
    else
        echo "0B/s"
    fi
}


# Get IP
network_ip=$(get_network_ip)

# Get Download Speed
get_download_speed=$(get_download_speed)

# Get CPU usage
cpu_usage=$(grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print int(usage)"%"}')

# Get memory usage
mem_usage=$(free | grep Mem | awk '{printf "%.1f%", $3/$2 * 100}')

# Get Battery
get_battery=$(get_battery)

echo " 🌐 $network_ip | 📥 $get_download_speed | 🧠 $cpu_usage | 🎞️ $mem_usage | $get_battery "
