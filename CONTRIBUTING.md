# Contributing to Omega Theory

Omega Theory is currently author-led. Contributions should improve traceability, reproducibility, criticism, or comparison rather than silently expanding the canon.

## Required structure for a proposed theoretical change

1. State the ontological premise.
2. Define every mathematical object and its domain.
3. Derive the result without importing the desired conclusion.
4. Provide numerical or symbolic checks when applicable.
5. Record counterexamples, failed tests, and parameter dependence.
6. Assign an epistemic status.
7. Explain which existing claims depend on the change.

## Numerical contributions

A numerical result should include:

- executable code;
- deterministic seed where appropriate;
- dependencies and versions;
- input parameters;
- generated outputs or a generation command;
- tolerances and failure criteria;
- a statement of what the test does **not** establish.

## Canon policy

Exploratory work belongs under `research/` until reviewed. Historical formulations are not deleted; they are marked as superseded or refuted. Familiar equations are not treated as derived merely because they occur in established physics.

## Issues and review

Use issues for narrowly scoped problems, counterexamples, reproducibility failures, and observational constraints. Major changes should be developed on a branch and reviewed through a pull request.
