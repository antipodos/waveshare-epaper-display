
. env.sh

function log {
    echo "---------------------------------------"
    echo ${1^^}
    echo "---------------------------------------"
}

log "Add weather info"
python3 screen-weather-get.py || exit 1

log "Add Calendar info"
python3 screen-calendar-get.py || exit 1

if [ -f screen-custom-get.py ]; then
    log "Add Custom data"
    python3 screen-custom-get.py || exit 1
elif [ ! -f screen-output-custom-temp.svg ]; then
    # Create temporary empty svg since the main SVG needs it
    echo "<svg />" > screen-output-custom-temp.svg
fi

log "Check if display needs updating"
NEW_HASH=$(sha256sum screen-output-weather.svg | cut -d' ' -f1)
OLD_HASH=""
if [ -f cache_display.hash ]; then
    OLD_HASH=$(cat cache_display.hash)
fi

if [ "$NEW_HASH" = "$OLD_HASH" ]; then
    log "No changes detected, skipping display refresh"
    exit 0
fi

log "Export to PNG"

if [ $WAVESHARE_EPD75_VERSION = 1 ]; then
    WAVESHARE_WIDTH=640
    WAVESHARE_HEIGHT=384
else
    WAVESHARE_WIDTH=800
    WAVESHARE_HEIGHT=480
fi

cairosvg -o screen-output.png -f png --dpi 300 --output-width $WAVESHARE_WIDTH --output-height $WAVESHARE_HEIGHT screen-output-weather.svg

log "Display on epaper"
python3 display.py screen-output.png && echo "$NEW_HASH" > cache_display.hash
