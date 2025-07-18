# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project develops tools and methodologies to automatically generate user documentation following the Diátaxis framework principles. The project contains:

- Original Diátaxis documentation in `diataxis-documentation-framework/` (READ-ONLY)
- Example documentation structure in `docs/` following the four Diátaxis categories
- Design specifications in `specs/design.md`

## Important Constraints

- **NEVER modify** any files in `diataxis-documentation-framework/` directory
- **NEVER add** new files to `diataxis-documentation-framework/` directory

## Diátaxis Framework Structure

The framework organizes documentation into four quadrants based on two dimensions:
- **Action vs. Cognition**: Practical (doing) vs. Theoretical (knowing)
- **Acquisition vs. Application**: Learning (study) vs. Applying (work)

### Documentation Types

1. **Tutorials** (`docs/tutorials/`) - Learning-oriented, hands-on experience
2. **How-to Guides** (`docs/how-to/`) - Goal-oriented, task completion
3. **Reference** (`docs/reference/`) - Information-oriented, technical descriptions
4. **Explanation** (`docs/explanation/`) - Understanding-oriented, conceptual discussions

### Key Implementation Principles

- **Strict Separation**: Never mix documentation types in a single document
- **User-Centric**: Each type serves specific user needs at specific times
- **Iterative Development**: Documentation should evolve continuously
- **Organic Structure**: Let structure emerge from well-formed content

## Architecture Notes

The project demonstrates:

- Example documentation in each Diátaxis category
- Design specs outlining the complete framework principles and techniques

When generating documentation:

- Use appropriate voice for each type (e.g., "we" for tutorials, neutral for reference)
- Follow the specific techniques outlined in `specs/design.md`
- Maintain clear boundaries between documentation types
- Cross-reference between related content across types

## Markdown Guidelines

Follow these guidelines when generating markdown.

- Generate "GitHub Flavored Markdown"
- Don't use emojis 
- When documenting a directory tree, use Unicode box drawing characters (`├──`, `│`, `└──`)
- When creating a markdown list, always add a blank line before the first entry
- Use four spaces for each markdown indent level For example:
```markdown

### MVP Features

- Data Input Flexibility

    - JSON configuration files with structured project/task format
    - Python dictionaries matching JSON schema
    - Comprehensive input validation and error handling
    - Automatic project timeline calculation

- Chart Generation

    - Clean, professional SVG output
    - Customizable styling and themes
    - Scalable vector graphics for any resolution
    - Lightweight file sizes

**Key Principles**:

- Testability and traceability over performance
- Pure functional core (no side effects)

```

### Markdown Examples

#### Bad Markdown has emojis, no blank before list start:
```
## ✨ What's New in v0.7.0

**New Feature: Novel Management Commands**

Book3 now includes comprehensive novel management capabilities:
- ✅ **Novel Removal**: Safely remove novels and all associated data with `book3 remove --novel ID`
- ✅ **Safety Features**: Confirmation prompts, detailed preview of data to be deleted, --force flag
- ✅ **Database Cleanup**: Complete removal of all related analysis data (chapters, scenes, characters, etc.)
- ✅ **Enhanced Export**: Improved export command with --novel parameter for consistency

**Goal**: Achieve 95%+ test coverage with zero mocks, complete observability, and deterministic testing.

**Key Principles**:
- Testability and traceability over performance
- Pure functional core (no side effects)

```

#### Good Markdown has no emojis, blank line before lists, four space indents:
```
## What's New in v0.7.0

New Feature: Novel Management Commands

Book3 now includes comprehensive novel management capabilities:

- Novel Removal: Safely remove novels and all associated data with `book3 remove --novel ID`
- Safety Features: Confirmation prompts, detailed preview of data to be deleted, --force flag
- Database Cleanup: Complete removal of all related analysis data (chapters, scenes, characters, etc.)
- Enhanced Export: Improved export command with --novel parameter for consistency

**Goal**: Achieve 95%+ test coverage with zero mocks, complete observability, and deterministic testing.

**Key Principles**:

- Testability and traceability over performance
- Pure functional core (no side effects)

```

