# cookiecuttercatfacts
awesommmeeeeeeeeeeeeeeeeeeeeeeeeeee

# Getting Started
## Prerequisites
cookiecuttercatfacts requires the following to be installed:
```
python >= 3.6
tox >= 2.9.1
docker
serverless
npm
nodejs
```

## Running Tests
`tox` will automatically execute linters as well as the unit tests.

To see all the available options, run `tox -l`.

## Deployment
* `npm install` The Serverless Framework project depends on a few plugins defined in `package.json`. This will install them.

* `sls create_domain -s <stage>` Create a user friendly domain name for the API Gateway. Do this only one time in each environment.

* `sls deploy -s <stage>` Stage is typically the environment such as `ci`/`production` or the account like `dev`/`prod`

* `sls invoke -s <stage> -f hello` The sample generated function is named `hello`. The `sls invoke` command can be used to test lambdas
directly before invoking them via a AWS event (API Gateway, SNS, Cloudwatch, etc)
