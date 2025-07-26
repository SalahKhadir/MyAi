# Assets Folder Structure

This folder contains all static assets for the Salah Khadir AI Portfolio application.

## Images Folder (`assets/images/`)

Place your project images here to be displayed in the portfolio. 

### Recommended Structure:
```
assets/
├── images/
│   ├── projects/
│   │   ├── ecotrace.png
│   │   ├── skillsync.png
│   │   ├── pharmacy-management.png
│   │   └── ai-chatbot.png
│   ├── profile/
│   │   └── profile-photo.jpg
│   └── logos/
│       ├── company-logos/
│       └── tech-stack/
```

### Image Guidelines:
- **Format**: PNG or JPG
- **Size**: Recommended 400x300px for project images
- **Quality**: High resolution for crisp display
- **Naming**: Use lowercase with hyphens (e.g., `my-project.png`)

### Usage in Code:
To use images in your project cards, update the `image_placeholder` field in projects_page.py:

```python
"image_placeholder": "assets/images/projects/ecotrace.png"
```

Or for profile photos in about_page.py:
```python
"profile_image": "assets/images/profile/profile-photo.jpg"
```

### Color Palette Reference:
- **Primary Blue**: #60a5fa
- **Secondary Blue**: #3b82f6
- **Green (Technologies)**: #10b981
- **Orange (Highlights)**: #f59e0b
- **Text Gray**: #94a3b8
- **Light Text**: #e2e8f0

Make sure your images complement this color scheme for a cohesive professional look.
