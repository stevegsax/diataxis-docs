# Generate User Documentation Using Diataxis Principles

The purpose of this project is to develop tools and methodologies that allow
us to automatically generate a set of user documentation that follows the
principles of the 
[Diataxis](https://github.com/evildmp/diataxis-documentation-framework.git) 
project.

- A copy of the original Diataxis project documentation is stored in subdirectory 
`diataxis-documentation-framework/`. 
- Do not modify any files in `diataxis-documentation-framework/`.

## Tasks 

1. [x] Review the diataxis framework and extract key principles. Write a succinct summary of each principle and list them below.
2. [x] Identify standard components of the diataxis solution and list them below
3. [x] Identify techniques used to generate each component and list them below


## Summary and Key Principles

The Diátaxis framework systematically organizes documentation into four distinct types based on two fundamental dimensions:

### Core Principle
Documentation serves different user needs at different times. The framework emerges from two dimensions:

- **Action vs. Cognition**: Whether documentation informs what users *do* (practical) or what they *know* (theoretical)
- **Acquisition vs. Application**: Whether users are *learning* their craft (study) or *applying* it (work)

### Key Principles

1. **Four Distinct Types**: Documentation must be strictly separated into tutorials, how-to guides, reference, and explanation
2. **User-Centric Design**: Each type serves a specific user need at a specific time
3. **Clear Boundaries**: Mixing documentation types creates confusion and reduces effectiveness
4. **Complete at Every Stage**: Documentation should be complete but never finished, like a living organism
5. **Iterative Development**: Work in small steps, improving documentation continuously
6. **Organic Structure**: Let structure emerge from well-formed content rather than top-down planning

## Standard Components

### 1. Tutorials (Learning-oriented)

- **Purpose**: Teaching through hands-on experience
- **User Need**: Learning and acquiring skills
- **Characteristics**: Step-by-step guidance, reliable outcomes, minimal explanation
- **Location**: `/docs/tutorials/`

### 2. How-to Guides (Goal-oriented)

- **Purpose**: Helping users accomplish specific tasks
- **User Need**: Solving real-world problems
- **Characteristics**: Task-focused, assumes competence, adaptable instructions
- **Location**: `/docs/how-to/`

### 3. Reference (Information-oriented)

- **Purpose**: Providing technical descriptions and facts
- **User Need**: Accurate information for work
- **Characteristics**: Neutral descriptions, structured like the product, authoritative
- **Location**: `/docs/reference/`

### 4. Explanation (Understanding-oriented)

- **Purpose**: Providing context and deepening understanding
- **User Need**: Understanding the bigger picture
- **Characteristics**: Discursive, discusses "why", includes alternatives
- **Location**: `/docs/explanation/`

### Supporting Elements

- **The Diátaxis Compass**: A decision tool for categorizing content
- **Cross-references**: Links between related content across types
- **Navigation structure**: Clear paths for users to find what they need

## Techniques

### Tutorial Techniques

1. **Show the destination first** - Tell learners what they'll achieve
2. **Deliver early wins** - Provide visible results quickly
3. **Maintain narrative flow** - Create a story of expectations
4. **Minimize explanation** - Focus on doing, not understanding
5. **Use concrete actions** - Avoid abstract concepts
6. **Encourage repetition** - Allow practice and reinforcement
7. **Use "we" language** - Establish teacher-learner relationship

### How-to Guide Techniques

1. **Clear goal titles** - "How to [achieve specific outcome]"
2. **Address complexity** - Handle real-world scenarios
3. **Provide adaptable steps** - Allow for different contexts
4. **Maintain logical flow** - Order steps sensibly
5. **Use conditional language** - "If you want X, do Y"
6. **Link to reference** - Point to additional options
7. **Focus on results** - Omit unnecessary completeness

### Reference Techniques

1. **Describe only** - No instruction or explanation
2. **Mirror architecture** - Structure follows the product
3. **Use consistent patterns** - Standardize format
4. **Include examples** - Illustrate usage
5. **State limitations** - Document constraints
6. **Provide warnings** - Note potential issues
7. **Be authoritative** - Present facts definitively

### Explanation Techniques

1. **Make connections** - Link concepts together
2. **Provide context** - Historical and design background
3. **Discuss alternatives** - Compare approaches
4. **Admit perspectives** - Acknowledge different views
5. **Use "about" framing** - Focus on understanding
6. **Include rationale** - Explain the "why"
7. **Allow reflection** - Give space for thought

### General Implementation Techniques

1. **The Diátaxis Compass** - Use the decision matrix to categorize content
2. **Iterative workflow** - Choose → Assess → Decide → Do → Repeat
3. **Cross-linking** - Connect related content across types
4. **User journey mapping** - Understand typical progression paths
5. **Language patterns** - Use appropriate voice for each type
6. **Continuous refinement** - Documentation is never finished
7. **Organic growth** - Let structure emerge from content
