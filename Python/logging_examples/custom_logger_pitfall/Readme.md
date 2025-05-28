This example shows a possible pitfall when using a custom logger.

Example unexpected_behavior.py shows
- using a custom logger instead of the root logger
- the log message at DEBUG level is suppressed despite setting the level of the logger
- this is caused by the logger using its parent which is the root logger which has a default level of warning

Example proper_behavior.py shows
- using a custom handler for the custom logger will remedy the problem
- setting the log level of the logger is still necessary
