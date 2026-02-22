# Phone Numbers Analyzer

A Python script that parses and analyzes phone numbers to extract timezone, geographic location, and carrier information.

## Overview

This project uses the `phonenumbers` library to validate and extract detailed information from phone numbers. It provides insights about the number's timezone, geographic location, and service carrier.

## Features

- **Timezone Detection**: Identifies the timezone(s) associated with the phone number
- **Geographic Location**: Determines the country/region where the number is registered
- **Carrier Identification**: Identifies the mobile network carrier
- **Number Validation**: Validates if the phone number is valid and possible

## Requirements

- Python 3.x
- `phonenumbers` library

## Installation

Install the required library using pip:

```
bash
pip install phonenumbers
```

## Usage

1. Run the script:
   
```
bash
   python PHONENUMBERS.py
   
```

2. Enter a mobile number with the country code when prompted (e.g., +14155552671)

3. The script will display:
   - Timezone(s) for the number
   - Geographic description (country/region)
   - Carrier name
   - Validation status (valid/possible)

## Example

```
Mobile no. with country code: +14155552671
('America/New_York',)
United States
Verizon Wireless
valid Mobile number: True
checking possibily of Number: True
```

## Code Explanation

| Function | Description |
|----------|-------------|
| `phonenumbers.parse()` | Parses the input string into a PhoneNumber object |
| `timezone.time_zones_for_number()` | Returns timezone(s) for the number |
| `geocoder.description_for_number()` | Returns geographic description |
| `carrier.name_for_number()` | Returns the carrier name |
| `phonenumbers.is_valid_number()` | Checks if the number is valid |
| `phonenumbers.is_possible_number()` | Checks if the number is possible |

## License

This project is for educational purposes.
