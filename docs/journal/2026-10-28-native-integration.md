# Grape Linux engineering journal: Native integration field report

**Event date:** 2026-10-28  
**Source:** Project owner development update  
**Event time:** Not independently captured for this public record  
**Classification:** New owner-reported progress and estimate addendum. Not a newly completed independent hardware validation.

## Revision history
The owner initially estimated overall native integration at approximately 80%, then revised it downward to a more conservative **68–72% range**. The present working figure is **70%**. The first assessment is preserved here as historical context, not the current estimate.

## Current reported capabilities
- Linux terminal and desktop can be used on the physical phone.
- Bluetooth is reported fully working.
- Battery power and charging are reported fully working.
- Wi-Fi is being connected and configured.
- Remaining native hardware work involves sound, cameras, storage, touch, GPS, radios, and related system interfaces.

These are owner-reported updates. The latest supporting logs and repeatable validation evidence have not been added to this public journal entry. Earlier dated test evidence, including charging and touch investigations, is not erased or silently replaced.

## Native hardware mapping
The immediate task is to identify radio and peripheral interfaces, document their Linux-facing mappings, and integrate their drivers and services into native system operation. A reusable, well-documented mapping approach could support research on other compatible iPhone models and firmware histories.

Compatibility on other hardware and iOS versions must be tested separately. The 70% estimate describes project-level integration progress, not a guarantee that 70% of each subsystem is functioning or that native autonomous cold boot has passed.

## Evidence to add
1. Terminal and desktop: dated device video showing actual interaction.
2. Bluetooth: pairing, data exchange and reconnect tests.
3. Power and charging: battery telemetry, sustained positive charging readings and logs.
4. Wi-Fi: association, addressing, network transfer and restart behavior.
5. Other devices: model-specific interface inventories and validation results.
6. Startup: physical cold-boot and restart traces.
7. Hardware status: test matrix with identified, mapped, integrated and validated states.

## Next review
Attach test logs, images, build identifiers and exact test timestamps. Update each hardware status from owner-reported to validated only when corresponding evidence is attached.
