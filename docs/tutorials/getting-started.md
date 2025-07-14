# Getting Started Tutorial

This tutorial will guide you through creating your first documentation project using the Diátaxis framework. By the end of this tutorial, you'll understand how to organize different types of documentation effectively.

## What You'll Learn

- How to set up a documentation structure
- The purpose of each documentation type
- How to write your first piece of documentation

## Prerequisites

- Basic familiarity with markdown
- A text editor
- Python 3.8 or later (for running the example code)

## Step 1: Understanding the Framework

The Diátaxis framework divides documentation into four types:

1. **Tutorials** - What you're reading now
2. **How-to guides** - Practical recipes
3. **Reference** - Technical descriptions
4. **Explanation** - Conceptual understanding

## Step 2: Create Your First Documentation

Let's start by creating a simple how-to guide. Create a new file called `docs/how-to/install-dependencies.md`:

```markdown
# How to Install Dependencies

To install the project dependencies:

1. Ensure you have Python 3.8+ installed
2. Run: `pip install -e ".[dev]"`
3. Verify installation: `python -c "import pytest; print('Success!')"` 
```

## Step 3: Run the Example Application

Our project includes a sample Python application that demonstrates documentation concepts:

```bash
python main.py
```

You should see output showing the four documentation types.

## Step 4: Explore the Structure

Take a moment to explore the `docs/` directory:

- `tutorials/` - Contains this getting started guide
- `how-to/` - Will contain task-oriented guides
- `reference/` - Will contain technical documentation
- `explanation/` - Will contain conceptual discussions

## Next Steps

Now that you understand the basic structure:

1. Read a how-to guide to accomplish a specific task
2. Check the reference documentation for technical details
3. Read the explanation documents to deepen your understanding

## What We've Learned

In this tutorial, you've:

- Created a documentation structure following Diátaxis
- Understood the four documentation types
- Run the example application
- Created your first piece of documentation

Remember: tutorials are about learning by doing, not just reading!