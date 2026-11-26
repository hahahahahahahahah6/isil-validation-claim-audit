# Library identifier claim audit

This offline static tool audits documented library-identifier claims against Python source calls. It examines root README prose and Markdown under docs, excluding fenced blocks; inline code counts. It normalises case, whitespace, hyphens and contractions, and removes negative matches before searching for positive matches. It never executes inspected code or contacts a network.

Install from a local distribution with `python3 -m pip install PATH`, then run:

```sh
isil-validation-claim-audit audit .
python3 -m isil_validation_claim_audit audit . --json
isil-validation-claim-audit --version
```

Use `--ignore PREFIX` repeatedly, `--fail-on medium` to include test-only findings in the exit threshold, and `--verbose` for the audited path. Exit status is 0 for pass, 2 for a finding at or above the threshold, and 1 for usage or I/O errors. The default threshold is high.

Positive claims without production evidence yield the following finding, with medium severity when evidence exists only in tests and high otherwise:

```
documented-isil-validation-claim-false
```

Negative claims with production evidence yield the following finding at high severity:

```
documented-no-isil-validation-claim-false
```

Evidence consists of statically recognised stdnum calls or named generic calls. Aliases are resolved and local shadows excluded. Tests count separately; fixtures, examples, docs, symlinks and syntax-invalid files do not supply production evidence. This is a heuristic; dead code counts, alias chains may be missed, each route must occur in one module, exact phrases are required and denial handling depends on the listed phrases.

## Differentiation

This audit does not cover generic input validation.
This audit does not cover ISBN book numbers.
This audit does not cover ISSN serial numbers.
This audit does not cover IBAN bank accounts.
This audit does not cover UUID strings.
This audit does not cover semantic versions.
This audit does not cover MAC addresses.
This audit does not cover BIC bank identifiers.
This audit does not cover cron expression validation.
This audit does not cover cron expression description.
This audit does not cover scheduled execution.
This audit does not cover calendar dates.
This audit does not cover timeouts.
This audit does not cover payment processing.
This audit does not cover credit card extraction.
This audit does not cover account authentication.
This audit does not cover password verification.
This audit does not cover password hashing.
This audit does not cover password generation.
This audit does not cover PDF encryption.
This audit does not cover email delivery.
This audit does not cover SMS delivery.
This audit does not cover document extraction.
This audit does not cover barcode decoding.
This audit does not cover email address validation.
This audit does not cover phone number validation.
This audit does not cover password strength.
This audit does not cover JSON Schema validation.
This audit does not cover credit card validation.
This audit does not cover domain validation.
This audit does not cover URL validation.
This audit does not cover IP address validation.
This audit does not cover JSON parsing.
This audit does not cover regular expression matching.
This audit does not cover URL parsing.
This audit does not cover web fetching.
This audit does not cover DNS lookup.
This audit does not cover barcode generation.
This audit does not cover account number extraction.
This audit does not cover vehicle number extraction.
This audit does not cover vehicle number decoding.
This audit does not cover vehicle history lookup.
This audit does not cover hex colour validation.
This audit does not cover ORCID researcher identifiers.
This audit does not cover DOI validation and resolution.
This audit does not cover CAS Registry Numbers.
This audit does not cover ISNI name identifiers.
This audit does not cover SEDOL security identifiers.
This audit does not cover ISIN security identifiers.
This audit does not cover security record lookup.
This audit does not cover security identifier extraction.
This audit does not cover IMEI identifiers.
This audit does not cover MEID identifiers.
This audit does not cover ESN identifiers.
This audit does not cover ISMN music publications.
This audit does not cover ISAN audiovisual works.
This audit does not cover GRid releases.
This audit does not cover EAN trade items.
This audit does not cover generic serial numbers.
This audit does not cover FIGI financial instruments.
This audit does not cover financial instrument lookup.
This audit does not cover financial instrument extraction.
This audit does not cover ISRC recordings.
This audit does not cover Ethereum addresses.
This audit does not cover Binance Smart Chain addresses.
This audit does not cover Tron addresses.
This audit does not cover Litecoin addresses.
This audit does not cover Dogecoin addresses.
This audit does not cover bitcoin addresses.
This audit does not cover transaction hashes.
This audit does not cover private keys.
This audit does not cover block explorer lookup.
This audit does not cover address generation.
This audit does not cover address extraction.
This audit does not cover payment receipt confirmation.
This audit does not cover spreadsheet reading.
This audit does not cover spreadsheet generation.
This audit does not cover word document reading.
This audit does not cover word document generation.
This audit does not cover presentation reading.
This audit does not cover presentation generation.
This audit does not cover PDF extraction.
This audit does not cover PDF generation.
This audit does not cover PDF merging.
This audit does not cover PDF splitting.
This audit does not cover PDF rotation.
This audit does not cover PDF form filling.
This audit does not cover PDF watermarking.
This audit does not cover PDF redaction.
This audit does not cover PDF compression.
This audit does not cover PDF annotation.
This audit does not cover table extraction.
This audit does not cover OCR.
This audit does not cover electronic signatures.
This audit does not cover screen recording.
This audit does not cover video generation.
This audit does not cover QR code generation.
This audit does not cover barcode scanning.
This audit does not cover audio mixing.
This audit does not cover audio generation.
This audit does not cover audio editing.
This audit does not cover audio source separation.
This audit does not cover speech recognition.
This audit does not cover text to speech.
This audit does not cover noise suppression.
This audit does not cover music generation.
This audit does not cover music transcription.
This audit does not cover InChI structures.
This audit does not cover SMILES molecular notation.
This audit does not cover EC inventory numbers.
This audit does not cover UN transport numbers.
This audit does not cover PubChem lookup.
This audit does not cover chemical structure validation.
This audit does not cover other chemical identifiers.
This audit does not cover CUSIP security identifiers.
This audit does not cover reading a container number from a shipping document.
This audit does not cover carrier registry lookup by container number.
This audit does not cover BIC registration of an owner code.
This audit does not cover container size and type codes.
This audit does not cover minting a fresh container number.
This audit does not cover ISO 6346 shipping-container numbers.
This audit does not cover fetching a library record from a registry over the network.
This audit does not cover registering a new library identifier with an agency.
This audit does not cover cataloguing library holdings or reading MARC records.
This audit does not cover looking a library up in OCLC or WorldCat.
This audit does not cover listing registered library identifier agencies.

## Limitations

```
validate isil
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
isil validation
```

The bare phrase above can denote a roadmap item; context requires human review.

```
isil validator
```

The bare phrase above can denote a hosted page; context requires human review.

```
isil check
```

The bare phrase above can denote a presence-only lint rule; context requires human review.

```
check isil
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
verify isil
```

The bare phrase above can denote visual confirmation of an organisation; context requires human review.

```
isil code validation
```

The bare phrase above can denote a field presence check; context requires human review.

```
valid isil
```

The bare phrase above can denote example output; context requires human review.

```
isil is valid
```

The bare phrase above can denote example output; context requires human review.

```
isil is invalid
```

The bare phrase above can denote example error text; context requires human review.

```
isil validity
```

The bare phrase above can denote a configuration flag or column name; context requires human review.

```
isil format validation
```

The bare phrase above can denote a format description; context requires human review.

```
validate isil number
```

The bare phrase above can denote a shape-only check; context requires human review.

```
isil number validation
```

The bare phrase above can denote a specification section; context requires human review.

```
validate isil code
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
check isil code
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
validate isil15
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
isil15 validation
```

The bare phrase above can denote a specification section; context requires human review.

```
isil number check
```

The bare phrase above can denote a catalogue checklist item; context requires human review.

```
isil validation
```

The bare phrase above can denote an external service result; context requires human review.

```
isil
```

The bare phrase above alone is not a claim match.

```
isil number
```

The bare phrase above alone is not a claim match.

```
validate identifier
```

The bare phrase above alone is not a claim match.

```
check digit
```

The bare phrase above alone is not a claim match.

```
library
```

The bare phrase above alone is not a claim match.

```
agency prefix
```

The bare phrase above alone is not a claim match.

```
ismn
```

The bare phrase above alone is not a claim match.

A compact call strips surrounding whitespace and does not judge a value.

A format call reformats a value and may uppercase its known agency, without judging it.

An EAN call judges a decimal barcode number; an EAN check digit calculation alone supplies no evidence.

A Luhn call judges a digit string; a Luhn check digit calculation alone supplies no evidence.

The identifier has no check digit; the library checks alphabet, length and agency prefix, but an empty or arbitrary second part can pass.

The library does not establish whether the second part is registered or whether the library exists.

Lowercase is accepted and returned unchanged, and surrounding whitespace is stripped.

Colons and slashes are permitted characters, but DE:1 and DE/1 fail the agency lookup because the entire value becomes the prefix.

A regular expression alone supplies no evidence.

A length check alone supplies no evidence.

An agency membership check alone supplies no evidence.

Calls for ISBN, ISSN, ISMN, ISAN and ISIN judge different identifiers.

A SEDOL call judges a seven character identifier.

A FIGI call judges a twelve character identifier.

An ISNI call judges a sixteen character identifier.

A CUSIP call judges a nine character identifier.

A GRid call judges an eighteen character identifier.

An ISRC call judges a twelve character recording code.

An IMEI call judges a fifteen digit identifier.

A registry lookup supplies no evidence.

A generation call does not judge an input.

The validators package has no route for this identifier.

The word library may refer to a software library.

Static analysis cannot establish whether a call runs.

A bare import supplies no evidence.

A bare name reference supplies no evidence.

A string literal supplies no evidence.

A comment supplies no evidence.

An external command supplies no evidence.

A roadmap item without code supplies no evidence.

Syntax-invalid files supply no evidence.
