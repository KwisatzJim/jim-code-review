# Shared review guidelines

Use the five perspectives as complementary questions, not quotas for findings. Missing tests, unfamiliar patterns, and theoretical risks are leads to investigate, not defects by themselves.

## Correctness

Trace inputs through state changes and outputs, including empty values, boundaries, partial failures, and repeated operations. Check ordering, error propagation, cancellation, concurrent updates, and assumptions invalidated by earlier mutations. At persistence boundaries, examine atomicity, lost updates, data loss, and recovery. Confirm the failing path is reachable under the project's actual contract.

## Security

Identify trust boundaries and attacker-controlled values. Trace those values to command execution, file access, queries, rendering, authentication, and authorization. Check credential exposure and permissions using the application's actual deployment and threat assumptions. A dangerous-looking API alone is not proof: establish control over its input and a consequential path. Redact secrets from reports.

## Architecture

Check compatibility with documented architecture and ownership of state or resources. Report structural problems only when there is a concrete maintenance consequence or explicit applicable project convention, with evidence. Do not turn preferences about naming, patterns, file size, or abstraction into bugs. Do not recommend broad rewrites when a local correction addresses the cause.

## Performance and reliability

Trace resource lifetimes, blocking work on interactive or asynchronous execution paths, repeated computation, unbounded growth, and failure recovery. State realistic workload or failure conditions and their consequence. Do not infer a meaningful performance problem solely from complexity notation or an extra allocation; show why it matters here. Check retries for duplicated side effects and missing limits.

## Platform and compatibility

Use declared targets and supported versions, not every possible platform. Inspect relevant filesystem, path, process, shell, dependency, API, packaging, and deployment assumptions. Verify platform guarantees before calling a difference a bug. Included assets do not alone establish platform support. Do not report lack of Windows support when the project supports only Linux/macOS.

## Evidence threshold

Keep a finding when code and verified contracts establish a reachable failure or meaningful convention violation. An executed test is useful but not mandatory. Try to refute every candidate before reporting it; do not require proof that a merely imagined scenario is impossible. Note unavailable verification honestly. Consolidate duplicate root causes across perspectives.

## Severity

Rate impact together with realistic triggering conditions, independently of confidence:

- **Critical:** demonstrated path to catastrophic impact, such as broad irreversible data loss or full compromise in the supported threat model, requiring urgent attention.
- **High:** substantial data loss, security breach, or failure of a core workflow under realistic conditions.
- **Medium:** meaningful incorrect behavior or reliability/maintenance problem with bounded impact or narrower conditions.
- **Low:** small but concrete actionable defect or documented convention violation with an explained maintenance consequence. Cosmetic preferences do not qualify.

Explain the rating when impact is not obvious. Do not inflate severity because validation is incomplete.
