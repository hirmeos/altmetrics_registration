# Altmetrics DOI regisration
[![Build Status](https://travis-ci.org/hirmeos/altmetrics_registration.svg?branch=master)](https://travis-ci.org/hirmeos/altmetrics_registration) [![Release](https://img.shields.io/github/release/hirmeos/altmetrics_registration.svg?colorB=58839b)](https://github.com/hirmeos/altmetrics_registration/releases) [![License](https://img.shields.io/github/license/hirmeos/altmetrics_registration.svg?colorB=ff0000)](https://github.com/hirmeos/altmetrics_registration/blob/master/LICENSE)

Obtain a list of DOIs and associated URLs from an instance of [hirmeos/identifier_translation_service][1] and register them with the [hirmeos/altmetrics][2] API.

This software may be useful to people who have set up an Identifier Translation Service in order to run any of the usage metrics drivers documented in [https://metrics.operas-eu.org/docs/getting-started][3]. If you are **not** intending to use the translation service for anything else you should use a different approach to register DOIs with the altmetrics API.

## Setup
### Requirements
- An instance of [hirmeos/identifier_translation_service][1] - you must first have a running version of this API.
- An [altmetrics user account][4].

## Run via crontab
```
0 0 * * 0 docker run --rm --name "altmetrics_registration" --env-file /path/to/config.env openbookpublishers/altmetrics_registration:1
```

[1]: https://github.com/hirmeos/identifier_translation_service "Identifier Translation Service"
[2]: https://github.com/hirmeos/altmetrics "Altmetrics Service"
[3]: https://metrics.operas-eu.org/docs/getting-started "Metrics docs"
[4]: https://docs.metrics.ubiquity.press/metrics/index.html "Almetrics user account"
