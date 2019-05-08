init:
	pipenv install --dev
	pipenv run install-lambda-functions

test:
	# Run unit tests
	# Fail if coverage falls below 95%
	pipenv run test

flake:
	# Make sure code conforms to PEP8 standards
	pipenv run flake8 {{cookiecutter.package_name}}
	pipenv run flake8 tests/unit tests/integration

lint:
	# Linter performs static analysis to catch latent bugs
	pipenv run lint --rcfile .pylintrc {{cookiecutter.package_name}}

# Command to run everytime you make changes to verify everything works
dev: flake lint test

# Verifications to run before sending a pull request
pr: init dev

ENV = dev
STACKNAME = $$(basename ${CURDIR})-$(ENV)-${USER}-stack
BUCKET = ${USER}-${ENV}-package-bucket
PROFILE = ${USER}
PACKAGED_TEMPLATE = .aws-sam/packaged-template.yaml
deploy:
	$(info Deploying to personal development stack)

    # Make sure we have a user-scoped credentials profile set. We don't want to be accidentally using the default profile
	@aws configure --profile ${PROFILE} list 1>/dev/null 2>/dev/null || (echo '\nMissing AWS Credentials Profile called '${PROFILE}'. Run `aws configure --profile ${PROFILE}` to create a profile called '${PROFILE}' with creds to your personal AWS Account'; exit 1)

    # Create bucket if it does not exist
	@aws --profile ${PROFILE} s3api head-bucket --bucket ${BUCKET} 2>/dev/null 1>/dev/null || aws --profile ${PROFILE} s3 mb s3://${BUCKET}

	sam build
	sam package --profile ${PROFILE} --s3-bucket $(BUCKET) --output-template-file $(PACKAGED_TEMPLATE)
	sam deploy --profile ${PROFILE} --template-file $(PACKAGED_TEMPLATE) --stack-name $(STACKNAME) --capabilities CAPABILITY_IAM

integ-test:
	# Integration tests don't need code coverage
	pipenv run pytest tests/integration --stack $(STACKNAME) --profile ${PROFILE} -s
