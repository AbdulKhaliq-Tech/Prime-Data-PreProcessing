# Services

Service boundaries for future business logic (Data Cleaning FR-02, Data
Customization FR-03, Data Extraction FR-04, Statistical Analysis FR-06,
Data Visualization FR-05, File Conversion FR-07, Word Report Generator
FR-08 [deferred until Phase 12], Mock Data Generation FR-09, Automation
FR-10, API Integration FR-11, Data Export FR-12).

Phase 00 intentionally leaves this package empty of business logic. Each
service module here should be added by the phase that owns the matching
functional requirement, and should implement the contracts defined in
`app/processing/contracts.py` where applicable.
