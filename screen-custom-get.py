import logging
from utility import update_svg, configure_logging, clean_text
from requests import get
import json

configure_logging()

def main():
    output_svg_filename = 'screen-output-weather.svg'
    url = "https://essensplan.netlify.app/plans/current/index.json"

    response = get(url)
    result = response.json()

    output_dict = {
        'CUSTOM_DATA_1' : clean_text(result['friday']),
	'CUSTOM_DATA_2' : clean_text(result['saturday']),
	'CUSTOM_DATA_3' : clean_text(result['sunday']),
	'CUSTOM_DATA_4' : clean_text(result['monday']),
	'CUSTOM_DATA_5' : clean_text(result['tuesday']),
	'CUSTOM_DATA_6' : clean_text(result['wednesday']),
	'CUSTOM_DATA_7' : clean_text(result['thursday'])
    }

    logging.info("custom: " + str(output_dict))

    logging.info("Updating SVG")
    update_svg(output_svg_filename, output_svg_filename, output_dict)

if __name__ == "__main__":
    main()
