# Swift and SwiftUI

Load for Swift changes. Establish deployment targets, Swift language mode, framework versions, and intended ownership of view/model state.

- Trace task completion after selection changes, view dismissal, cancellation, or model replacement. Show how stale work can update the wrong state or lose a user edit.
- Inspect actor isolation and UI updates against the project's concurrency mode and SDK contracts. Do not infer a data race merely because code is asynchronous.
- Check closure and observer lifetimes for a concrete retention cycle or unremoved long-lived subscription. A strong capture by itself does not prove a leak.
- Trace optional handling, collection access, and persistence failures to a reachable crash or incorrect result. Respect deliberate assertions with established preconditions.
- Check API availability on supported OS versions, file access under the application's sandbox, and resource cleanup after failed media/file operations. Do not report an absent entitlement without identifying the operation and applicable requirement.
