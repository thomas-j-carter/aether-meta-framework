# AETHER Rules v3: Resilience
- **Inherit:** All v2 Rules.
- **Diagnosis First:** If a test fails, AI must provide: 1. Observed, 2. Expected, 3. Hypothesis, 4. Proposed Fix.
- **Defensive Design:** Errors (like corrupt files) must be handled gracefully without crashing the core loop.
