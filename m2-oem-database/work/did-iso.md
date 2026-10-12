# ISO 14229-1 Standard UDS Data Identifier (DID) Catalog

Research for the M2 OEM vehicle database (v1.3). Standardized DIDs from
ISO 14229-1:2013 Table C.1 (Annex C, normative), verified against the
standard text. Every claim carries a quality grade: **A** = ISO 14229-1:2013
text · **B** = reputable UDS reference with multi-source agreement ·
**C** = single community source. Research date: 2026-10-06.

Key ISO facts used throughout (all [A] — ISO 14229-1:2013):
- Record-data content and format for identification DIDs is
  "server specific" (ECU/OEM defined) unless the standard says otherwise.
  ISO fixes the DID *number and name*, not the record length, for most DIDs.
- 0xF180/0xF181/0xF182: first record-data byte is numberOfModules, then the
  per-module identification(s).
- Dates (0xF18B, 0xF199, 0xF19B, 0xF19D): unsigned numeric, ASCII or BCD,
  ordered Year, Month, Day.
- 0xF190 VIN: the standard's own scaling example computes the record length
  as 17 data bytes.
- The "Cvt" column in Table C.1 marks each entry U or M (ISO conformance
  annotation; legend not verified from the excerpt — not interpreted here).

Session/security (general): ISO does not normatively tie identification DIDs
to a session or security level — that is server/OEM defined. In practice the
identification DIDs below are readable in the default session without security
access on most production ECUs [B — ISO 0x22 example assumes the client "may
request a dataIdentifier at any time independent of the status of the server";
example-ECU docs show identification DIDs readable at security level 0; VIN
0xF190 is readable by generic tools everywhere]. Some OEMs gate individual
DIDs (notably fingerprints) behind extended session or security access [C].

---

## 0xF180
- Name: BootSoftwareIdentificationDataIdentifier
- Description: ECU boot software identification record; first data byte is numberOfModules, followed by the boot software identification(s)
- Size: variable — 1 byte count + ECU-specific structures (not fixed by ISO)
- Session: default (server-defined; readable in default session on most ECUs) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic BSIDID)

## 0xF181
- Name: applicationSoftwareIdentificationDataIdentifier
- Description: ECU application software number(s); first data byte is numberOfModules, followed by the application software identification(s)
- Size: variable — 1 byte count + ECU-specific structures (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ASIDID)

## 0xF182
- Name: applicationDataIdentificationDataIdentifier
- Description: ECU application data (calibration) identification record; first data byte is numberOfModules, followed by the application data identification(s)
- Size: variable — 1 byte count + ECU-specific structures (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ADIDID)

## 0xF183
- Name: bootSoftwareFingerprintDataIdentifier
- Description: ECU boot software fingerprint record (e.g. records which tool last programmed the boot software); content/format ECU-specific
- Size: ECU-specific (not fixed by ISO)
- Session: default on many ECUs; some OEMs require extended session [C]
- Security: none required by ISO; some OEMs gate behind security access [C]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic BSFPDID)

## 0xF184
- Name: applicationSoftwareFingerprintDataIdentifier
- Description: ECU application software fingerprint record; content/format ECU-specific
- Size: ECU-specific (not fixed by ISO)
- Session: default on many ECUs; some OEMs require extended session [C]
- Security: none required by ISO; some OEMs gate behind security access [C]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ASFPDID)

## 0xF185
- Name: applicationDataFingerprintDataIdentifier
- Description: ECU application data fingerprint record; content/format ECU-specific
- Size: ECU-specific (not fixed by ISO)
- Session: default on many ECUs; some OEMs require extended session [C]
- Security: none required by ISO; some OEMs gate behind security access [C]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ADFPDID)

## 0xF186
- Name: ActiveDiagnosticSessionDataIdentifier
- Description: Reports the server's currently active diagnostic session; value is the diagnosticSessionType subfunction (0x01=default, 0x02=programming, 0x03=extended, 0x04=safety system)
- Size: 1 byte [B]
- Session: default [B]
- Security: none required [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ADSDID); 1-byte size corroborated by multiple UDS references and a real-ECU capture returning a single byte

## 0xF187
- Name: vehicleManufacturerSparePartNumberDataIdentifier
- Description: Vehicle manufacturer spare part number; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic VMSPNDID)

## 0xF188
- Name: vehicleManufacturerECUSoftwareNumberDataIdentifier
- Description: Vehicle manufacturer ECU (server) software number; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic VMECUSNDID)

## 0xF189
- Name: vehicleManufacturerECUSoftwareVersionNumberDataIdentifier
- Description: Vehicle manufacturer ECU (server) software version number; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic VMECUSVNDID)

## 0xF18A
- Name: systemSupplierIdentifierDataIdentifier
- Description: System (Tier-1) supplier name and address information; content/format defined by the system supplier
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic SSIDDID)

## 0xF18B
- Name: ECUManufacturingDateDataIdentifier
- Description: ECU (server) manufacturing date, ordered Year, Month, Day
- Size: not fixed by ISO; encoding unsigned numeric, ASCII or BCD [A]
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ECUMDDID)

## 0xF18C
- Name: ECUSerialNumberDataIdentifier
- Description: ECU (server) serial number; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ECUSNDID)

## 0xF18D
- Name: supportedFunctionalUnitsDataIdentifier
- Description: Functional units implemented in the server (capability bitmap)
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic SFUDID)

## 0xF18E
- Name: VehicleManufacturerKitAssemblyPartNumberDataIdentifier
- Description: Vehicle manufacturer order number for a kit (assembled parts bought as a whole, e.g. cockpit) where the spare part number designates only the server; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic VMKAPNDID)

## 0xF18F
- Name: ISOSAEReservedStandardized
- Description: Reserved by ISO for future definition of standardized identification options — not assigned
- Size: n/a
- Session: n/a
- Security: n/a
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ISOSAERESRVD)

## 0xF190
- Name: VINDataIdentifier
- Description: Vehicle Identification Number; content/format specified by the vehicle manufacturer (17 characters in practice)
- Size: 17 bytes, ASCII [A for 17 — ISO's own scaling example; B for ASCII — white papers and ECU examples agree]
- Session: default [B]
- Security: none required [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic VINDID); Softing UDS white paper (VIN "consists of 17 bytes"); udsoncan example decodes 17 chars

## 0xF191
- Name: vehicleManufacturerECUHardwareNumberDataIdentifier
- Description: Vehicle manufacturer specific ECU (server) hardware number; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic VMECUHNDID)

## 0xF192
- Name: systemSupplierECUHardwareNumberDataIdentifier
- Description: System supplier specific ECU (server) hardware number; content/format defined by the system supplier
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic SSECUHWNDID)

## 0xF193
- Name: systemSupplierECUHardwareVersionNumberDataIdentifier
- Description: System supplier specific ECU (server) hardware version number; content/format defined by the system supplier
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic SSECUHWVNDID)

## 0xF194
- Name: systemSupplierECUSoftwareNumberDataIdentifier
- Description: System supplier specific ECU (server) software number; content/format defined by the system supplier
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic SSECUSWNDID)

## 0xF195
- Name: systemSupplierECUSoftwareVersionNumberDataIdentifier
- Description: System supplier specific ECU (server) software version number; content/format defined by the system supplier
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic SSECUSWVNDID)

## 0xF196
- Name: exhaustRegulationOrTypeApprovalNumberDataIdentifier
- Description: Exhaust regulation or type approval number (for systems requiring type approval); content/format server-specific, subject to legislation
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic EROTANDID)

## 0xF197
- Name: systemNameOrEngineTypeDataIdentifier
- Description: System name or engine type; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic SNOETDID)

## 0xF198
- Name: repairShopCodeOrTesterSerialNumberDataIdentifier
- Description: Repair shop code or tester (client) serial number, e.g. identifying the most recent service client that reprogrammed server memory; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic RSCOTSNDID)

## 0xF199
- Name: programmingDateDataIdentifier
- Description: Date when the server was last programmed, ordered Year, Month, Day
- Size: not fixed by ISO; encoding unsigned numeric, ASCII or BCD [A]
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic PDDID)

## 0xF19A
- Name: calibrationRepairShopCodeOrCalibrationEquipmentSerialNumberDataIdentifier
- Description: Repair shop code or client serial number, e.g. identifying the most recent service client that recalibrated the server; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic CRSCOCESNDID)

## 0xF19B
- Name: calibrationDateDataIdentifier
- Description: Date when the server was last calibrated, ordered Year, Month, Day
- Size: not fixed by ISO; encoding unsigned numeric, ASCII or BCD [A]
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic CDDID)

## 0xF19C
- Name: calibrationEquipmentSoftwareNumberDataIdentifier
- Description: Software version of the client equipment used to calibrate the server; content/format server-specific
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic CESWNDID)

## 0xF19D
- Name: ECUInstallationDateDataIdentifier
- Description: Date when the ECU (server) was installed in the vehicle, ordered Year, Month, Day
- Size: not fixed by ISO; encoding unsigned numeric, ASCII or BCD [A]
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic EIDDID)

## 0xF19E
- Name: ODXFileDataIdentifier
- Description: References the ODX (Open Diagnostic Data Exchange) file of the server used to interpret and scale the server's data
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic ODXFDID)

## 0xF19F
- Name: EntityDataIdentifier
- Description: Entity data identifier for a secured data transmission (used with SecuredDataTransmission 0x84)
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic EDID)

## 0xFA10
- Name: NumberOfEDRDevices
- Description: Number of Event Data Recorder devices capable of reporting EDR data
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic NOEDRD)

## 0xFA11
- Name: EDRIdentification
- Description: EDR identification data
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic EDRI)

## 0xFA12
- Name: EDRDeviceAddressInformation
- Description: EDR device address information, per the format ISO 26021-2 defines for its DID 0xFA02
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic EDRDAI)

## 0xFF00
- Name: UDSVersionDataIdentifier
- Description: UDS version implemented in the server (scaling defined in ISO Table C.5/C.11)
- Size: server-specific (not fixed by ISO)
- Session: default (server-defined) [B]
- Security: none required by ISO; server-defined [B]
- Grade: [A]
- Evidence: ISO 14229-1:2013 Table C.1 (mnemonic UDSVDID)

---

## DID range map (ISO 14229-1:2013 Table C.1) [A]

| Range | Designation | Notes |
|---|---|---|
| 0x0000–0x00FF | ISOSAEReserved | Reserved for future definition |
| 0x0100–0xA5FF | VehicleManufacturerSpecific | OEM record/IO DIDs |
| 0xA600–0xA7FF | ReservedForLegislativeUse | Future legislation |
| 0xA800–0xACFF | VehicleManufacturerSpecific | OEM record/IO DIDs |
| 0xAD00–0xAFFF | ReservedForLegislativeUse | Future legislation |
| 0xB000–0xB1FF | VehicleManufacturerSpecific | OEM record/IO DIDs |
| 0xB200–0xBFFF | ReservedForLegislativeUse | Future legislation |
| 0xC000–0xC2FF | VehicleManufacturerSpecific | OEM record/IO DIDs |
| 0xC300–0xCEFF | ReservedForLegislativeUse | Future legislation |
| 0xCF00–0xEFFF | VehicleManufacturerSpecific | OEM record/IO DIDs |
| 0xF000–0xF00F | networkConfigurationDataForTractorTrailerApplication | Trailer remote addresses |
| 0xF010–0xF0FF | vehicleManufacturerSpecific | OEM record/IO DIDs |
| 0xF100–0xF17F | identificationOptionVehicleManufacturerSpecific | VM identification options — NOT standardized, VM-defined |
| 0xF180–0xF19E | Standardized identification DIDs | The per-DID entries above |
| 0xF19F | EntityDataIdentifier | Secured data transmission |
| 0xF1A0–0xF1EF | identificationOptionVehicleManufacturerSpecific | VM-defined |
| 0xF1F0–0xF1FF | identificationOptionSystemSupplierSpecific | Supplier-defined |
| 0xF200–0xF2FF | periodicDataIdentifier | Static or dynamic periodic DIDs |
| 0xF300–0xF3FF | DynamicallyDefinedDataIdentifier | 0x2C-defined DIDs |
| 0xF400–0xF4FF | OBDDataIdentifier | ISO 15031-5 PIDs |
| 0xF500–0xF5FF | OBDDataIdentifier | Future OBD PIDs |
| 0xF600–0xF6FF | OBDMonitorDataIdentifier | ISO 15031-5 monitor results |
| 0xF700–0xF7FF | OBDMonitorDataIdentifier | Future monitor results |
| 0xF800–0xF8FF | OBDInfoTypeDataIdentifier | ISO 15031-5 info types (incl. VIN/CALID/CVN) |
| 0xF900–0xF9FF | TachographDataIdentifier | ISO 16844-7 |
| 0xFA00–0xFA0F | AirbagDeploymentDataIdentifier | ISO 26021-2 (pyrotechnic end-of-life) |
| 0xFA13–0xFA18 | EDREntries | Individual EDR entries, FA13 = latest |
| 0xFA19–0xFAFF | SafetySystemDataIdentifier | Safety-system DIDs |
| 0xFB00–0xFCFF | ReservedForLegislativeUse | Future legislation |
| 0xFD00–0xFEFF | SystemSupplierSpecific | Supplier record/IO DIDs |
| 0xFF00 | UDSVersionDataIdentifier | Per-DID entry above |
| 0xFF01–0xFFFF | ISOSAEReserved | Reserved for future definition |

---

## Sources consulted

- ISO 14229-1:2013(E), Table C.1 "DID parameter definitions" (via testerpresent.com.au PDF mirror) — DID numbers, names, mnemonics, format rules, ranges [A]. Brief paraphrases only; no substantial text reproduced.
- Softing Automotive white paper WP1903 "Unified Diagnostic Services" (via testerpresent.com.au) — DID examples (F180/F18C/F190), VIN 17-byte worked example [B]
- pylessard/python-udsoncan docs (github.com) — 0x22 usage, VIN 17-char decode example [B]
- shaikirfandev/capll UDS guide (github.com) — standardized DID range table, critical-DID list [C]
- sagarembedded/learn_udsprotocol (github.com) — DID range purposes, 0xF186 1-byte note [C]
- xaloqi/eds safeboot ECU examples (github.com) — per-DID sizes on an example ECU, default-session readability note [C]
- icanhack.nl BlockHarbor CTF 2025 writeup — real ECU returning 0xF186/0xF187/0xF18A during default-session enumeration [C]

## Conflicts and corrections (reported, not silently resolved)

1. The research brief's name list is shifted vs ISO 14229-1:2013 Table C.1 for several DIDs: brief "0xF194 ODXFileIdentifier" → ISO 0xF194 is systemSupplierECUSoftwareNumberDataIdentifier (ODX is 0xF19E); brief "0xF196 SoftwareDownloadDate" → ISO 0xF196 is exhaustRegulationOrTypeApprovalNumberDataIdentifier; brief "0xF19B CalibrationEquipmentSoftwareNumber" → ISO 0xF19B is calibrationDateDataIdentifier; brief "0xF19C VehicleManufacturerECUHardwareNumber" → ISO 0xF19C is calibrationEquipmentSoftwareNumberDataIdentifier; brief "0xF19D SystemSupplierECUHardwareNumber" → ISO 0xF19D is ECUInstallationDateDataIdentifier; brief "0xF19E SystemSupplierECUHardwareVersionNumber" → ISO 0xF19E is ODXFileDataIdentifier; brief "0xF195 EntityIdentifier" → ISO 0xF195 is systemSupplierECUSoftwareVersionNumberDataIdentifier (Entity is 0xF19F). ISO names are used throughout.
2. Community guides remap some DIDs differently: capll lists 0xF197 as vehicleManufacturerVehicleType, 0xF198 as applicationSoftwareFingerprint, 0xF199 as applicationDataFingerprint, 0xF19D as programmedState, 0xF19E as calDataODX — all conflict with ISO Table C.1; ISO is authoritative.
3. sagarembedded/learn_udsprotocol lists 0xF18C as "ECU Calibration Identification Number" and 0xF18E as "ECU Serial Number" — ISO assigns ECUSerialNumber to 0xF18C and the kit assembly part number to 0xF18E. ISO used.
4. sagarembedded claims programming session = 0x10; ISO 14229-1 defines diagnosticSessionType 0x02 = programmingSession (0x10 is the service ID). ISO used.
5. 0xF100–0xF17F is NOT a standardized range — ISO designates it vehicle-manufacturer-specific identification options, despite some community tables implying standard content.

## Coverage notes

- Record lengths: ISO fixes almost no DID record lengths (exceptions: VIN 17 bytes per the standard's scaling example; 0xF180–0xF182 first byte = numberOfModules; 0xF186 = 1 byte per multi-source agreement). All other sizes are server-specific — marked as such rather than invented.
- Session/security per DID: not normatively fixed by ISO; marked per-entry as server-defined with the practical default-session note [B/C].
- ISO 14229-1:2020 (3rd edition) may have added standardized DIDs beyond this 2013 list — not verified in this pass [?].
- Make-specific DID catalogs (Toyota/Honda/VW/Hyundai/Nissan/Ford/GM/Stellantis 0x0100+ and 0xF1xx ranges) are a separate v1.3 work item, not covered here.
- The "Cvt" column legend (U/M) in Table C.1 was not verified from the excerpt and is not interpreted.
