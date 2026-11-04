# Rust

Load for Rust changes. Check the manifest, lockfile, supported toolchain, and actual caller contracts before relying on library behavior.

- Trace `Result` and `Option` handling across the user-visible operation. For `unwrap`, indexing, and arithmetic, identify a reachable invalid value before reporting a panic; test-only assertions and proven invariants are not findings by themselves.
- Check ownership of locks, guards, tasks, files, and transactions through early returns and cancellation. Identify a concrete lock order or execution sequence for deadlock/race findings. Do not assume a guard's lifetime from its variable name.
- For asynchronous paths, inspect blocking work and cancellation boundaries relative to the runtime and workload. Do not demand asynchronous code where the framework already offloads work.
- For `unsafe` or foreign interfaces, check the relied-on initialization, alignment, lifetime, aliasing, and thread guarantees, including changes outside the unsafe block that invalidate them. Verify the relevant contracts before alleging unsoundness.
- Preserve supported feature combinations and target-specific dependencies. Missing documentation or a different error type alone does not establish a defect.
