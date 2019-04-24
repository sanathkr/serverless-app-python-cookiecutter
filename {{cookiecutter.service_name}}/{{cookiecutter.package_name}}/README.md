Entrypoint for the Lambda function. Need a separate file like this in order to work around problem of relative imports.
Lambda's Python loader does not set a parent module when loading the handler file. Therefore relative imports won't
work within the handler
