This example shows a possible pitfall when using a custom logger.

With unexpected_behavior.py it shows
- using a custom logger instead of the root logger
- the log message at DEBUG level is suppressed despite setting the level of the logger
- this is caused by using the default handler which has a level of its own, by default WARNING

With proper_behavior.py it shows
- using a custom handler will remedy the problem
