# How to Add New Documentation

This guide shows you how to add new documentation to your project following the Diátaxis framework.

## Determine Documentation Type

First, identify which type of documentation you're writing:

- **Tutorial**: Teaching someone who's never done it before
- **How-to**: Helping someone accomplish a specific task
- **Reference**: Documenting technical specifications
- **Explanation**: Discussing concepts and providing context

## Create the File

1. Navigate to the appropriate directory:
   ```bash
   cd docs/[type]/  # where [type] is tutorials, how-to, reference, or explanation
   ```

2. Create a new markdown file with a descriptive name:
   ```bash
   touch meaningful-filename.md
   ```

## Write the Content

### For Tutorials

Start with learning objectives and prerequisites:

```markdown
# Tutorial Title

## What You'll Learn
- Objective 1
- Objective 2

## Prerequisites
- Required knowledge
- Required tools

## Step 1: First Step
[Detailed instructions...]
```

### For How-to Guides

Be direct and task-focused:

```markdown
# How to [Accomplish Task]

## Prerequisites
- What's needed before starting

## Steps
1. Do this first
2. Then do this
3. Finally do this

## Verification
How to verify success
```

### For Reference Documentation

Be precise and comprehensive:

```markdown
# [Component] Reference

## Overview
Brief description

## API/Interface
Detailed specifications

## Parameters
| Name | Type | Description |
|------|------|-------------|
| param1 | str | Description |

## Examples
```

### For Explanations

Focus on understanding:

```markdown
# Understanding [Concept]

## Introduction
Why this matters

## Background
Historical context or theoretical foundation

## How It Works
Detailed explanation

## Implications
What this means for users
```

## Review Checklist

Before finalizing:

- [ ] Is it in the correct directory?
- [ ] Does it follow the appropriate template?
- [ ] Is the filename descriptive?
- [ ] Have you linked to it from other relevant docs?
- [ ] Is the language appropriate for the documentation type?

## Common Mistakes to Avoid

- Don't mix documentation types in one file
- Don't assume knowledge in tutorials
- Don't include explanations in how-to guides
- Don't omit examples from reference docs