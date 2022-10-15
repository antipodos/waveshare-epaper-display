import logging
from utility import update_svg, configure_logging

configure_logging()

def main():
    output_svg_filename = 'screen-output-weather.svg'

    # If you make changes to this file be sure to make a backup in case you ever update! 
    
    # Add custom code here like getting PiHole Status, car charger status, API calls. 
    # Assign the value you want to display to custom_value_1, and it will replace CUSTOM_DATA_1 in screen-custom.svg.
    # You can edit the screen-custom.svg to change appearance, position, font size, add more custom data. 
    custom_value_1 = "";

    logging.info("Updating SVG")
    output_dict = {
        'CUSTOM_DATA_1' : 'bestellen',
	'CUSTOM_DATA_2' : 'Pizza',
	'CUSTOM_DATA_3' : 'Topfenpalatschinken',
	'CUSTOM_DATA_4' : 'kalt',
	'CUSTOM_DATA_5' : 'Baguettes',
	'CUSTOM_DATA_6' : 'Kürbisrisotto',
	'CUSTOM_DATA_7' : 'Nudeln + Pesto'
    }
    update_svg(output_svg_filename, output_svg_filename, output_dict)

if __name__ == "__main__":
    main()
