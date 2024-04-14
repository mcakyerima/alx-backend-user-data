#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    """
    Returns the log message obfuscated.

    Arguments:
        fields: list of strings representing all fields to obfuscate
        redaction: string representing the replacement for the obfuscated field
        message: string representing the log line
        separator: string representing the separator between fields in the log line

    Returns:
        The log message with specified fields obfuscated.
    """
    for field in fields:
        # Create a regex pattern to match the field and its value
        pattern = r'{}=.*?{}'.format(re.escape(field), re.escape(separator))
        # Replace the field's value with the redaction
        message = re.sub(pattern, '{}={}'.format(field, redaction) + separator, message)
    return message
