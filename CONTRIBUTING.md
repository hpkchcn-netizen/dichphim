# Contributing to DichPhim

Thank you for your interest in contributing to DichPhim! This document provides guidelines for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on the code, not the person
- Help others learn and grow
- Report issues professionally

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/dichphim.git
cd dichphim
git remote add upstream https://github.com/hpkchcn-netizen/dichphim.git
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/your-bug-fix
```

Branch naming conventions:
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation
- `test/description` - Tests

### 3. Development Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Install dev tools
pip install -e ".[dev]"
```

## Making Changes

### Code Style

We follow PEP 8 with Black for formatting:

```bash
# Format your code
black dichphim/ tests/

# Check style
flake8 dichphim/ tests/

# Type checking
mypy dichphim/
```

### Commit Messages

Use clear, descriptive commit messages:

```
<type>: <short summary> (<max 50 chars)

<detailed explanation if needed>

Fixes #<issue_number> (if applicable)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Tests
- `chore`: Build/CI/dependencies

### Example Commit

```
feat: add batch video processing support

- Implement BatchProcessor class
- Add queue management for parallel processing
- Support progress tracking across batches

Fixes #42
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_audio.py

# Run with coverage
pytest --cov=dichphim
```

### Writing Tests

```python
# tests/test_feature.py
import pytest
from dichphim import YourClass

class TestYourFeature:
    def setup_method(self):
        """Setup test fixtures"""
        self.instance = YourClass()
    
    def test_basic_functionality(self):
        """Test basic behavior"""
        result = self.instance.method()
        assert result is not None
    
    def test_error_handling(self):
        """Test error cases"""
        with pytest.raises(ValueError):
            self.instance.method(invalid_arg)
```

## Documentation

### Docstrings

Use Google-style docstrings:

```python
def process_video(input_path: str, output_path: str) -> Dict[str, Any]:
    """Process a video file for dubbing.
    
    Args:
        input_path: Path to input video file
        output_path: Path for output dubbed video
    
    Returns:
        Dictionary containing processing results with keys:
            - 'success': bool
            - 'output_path': str
            - 'duration': float (seconds)
            - 'metadata': dict
    
    Raises:
        FileNotFoundError: If input video not found
        ValueError: If format not supported
    """
```

### README Updates

If adding features, update README.md with:
- Feature description
- Usage example
- Any new dependencies

## Submitting Changes

### 1. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 2. Create a Pull Request

On GitHub, click "New Pull Request" and:

1. **Title:** Clear, descriptive title
2. **Description:** Include:
   - What changes were made
   - Why these changes
   - How to test
   - Screenshots/videos if applicable
   - Closes #<issue_number>

### 3. PR Checklist

- [ ] Code follows style guide (black, flake8)
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Commits have clear messages
- [ ] No breaking changes (or discussed)
- [ ] Works locally

### Example PR Description

```markdown
## Description
Adds support for batch video processing with parallel execution.

## Changes
- Added `BatchProcessor` class
- Implemented work queue with thread pool
- Added progress tracking and error handling

## Testing
- Added 15 new unit tests
- Tested with batch of 10 videos
- Performance improved 3x on quad-core system

## Screenshots
[Screenshot showing progress UI]

Closes #123
```

## Review Process

1. **Automated Checks:** Tests and style must pass
2. **Code Review:** Maintainers review changes
3. **Feedback:** Address review comments
4. **Approval:** Two approvals required
5. **Merge:** Squash and merge to main

## Areas to Contribute

### High Priority
- [ ] Improve lip-sync accuracy
- [ ] Add more language support
- [ ] Performance optimization
- [ ] Better error messages

### Medium Priority
- [ ] Web UI
- [ ] API documentation
- [ ] Video tutorials
- [ ] Example scripts

### Low Priority
- [ ] Code examples
- [ ] Translation improvements
- [ ] Minor optimizations

## Questions?

- 💬 [GitHub Discussions](https://github.com/hpkchcn-netizen/dichphim/discussions)
- 📧 Email: hpkchcn@gmail.com
- 🐛 [Issue Tracker](https://github.com/hpkchcn-netizen/dichphim/issues)

Thank you for contributing! 🎉