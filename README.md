![GitHub Docker Action Template](doc/logo.png)

[Introduction](#introduction) -
[Usage](#usage) -
[About](#about)



<a name="introduction"/>

## Introduction

Introduction

<a name="usage"/>

## Usage

### GitHub Action

#### Secrets

The following secrets can be set per GitHub Organisation, or per Repository.

input:

Name | Required | Action Reference | Example
---- | -------- | ---------------- | -------

output:
Name | Reference
---- | ---------

#### Workflow Action

```yaml
name: test_scan

on:  
  push:

env:
  ...

jobs:
  unitTesting:
    runs-on: [ Linux-sl3 ]
    steps:
        - name: Checkout Repository
          uses: actions/checkout@v2

        - name: bash
          uses: action-repo@tag
          with:
            ...

```
## About

### Maintainers

* [Huy.LeDang@vn.bosch.com](mailto:Huy.LeDang@vn.bosch.com)



### Third-party Licenses

| Name | License | Type |
|------|---------|------|


### Used Encryption

None.
