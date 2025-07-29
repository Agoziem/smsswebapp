# SMSS School Website Design System Reference

## Overview
This document outlines the comprehensive design patterns, color schemes, spacing, and styling conventions used throughout the SMSS school website project. This serves as a reference for maintaining consistency across all pages and components.

## 🎨 Color Palette & Theme

### Primary Colors
- **Wine Red (Primary)**: `#3b0505` - Main brand color
  - Usage: Headers, primary buttons, borders, accents
  - TailwindCSS: `bg-primary`, `text-primary`, `border-primary`
  - Opacity variants: `bg-primary/20`, `bg-primary/10`, `bg-primary/5`

### Secondary Colors
- **Orange (Secondary)**: `rgb(250, 178, 44)` - Accent color
  - Usage: Management team cards, secondary buttons, highlights
  - TailwindCSS: `bg-secondary`, `text-secondary`

### Royal Blue Theme (Teachers Section)
- **Royal Blue**: `#011b4d` - Teachers section theme
  - Usage: Teacher cards, teacher navigation
  - TailwindCSS: `bg-royal-blue`, `text-royal-blue`

### Neutral Colors
- **White**: `#ffffff` - Base background
  - TailwindCSS: `bg-base-100`, `bg-white`
- **Dark Cream**: `#e5d5b5` - Section backgrounds
  - TailwindCSS: `bg-dark-cream`
- **Gray variants**: For text and subtle elements
  - TailwindCSS: `text-gray-500`

## 📐 Layout Patterns

### Container System
```html
<!-- Primary container for most sections -->
<div class="auto-container">
  <!-- Content -->
</div>

<!-- Alternative full-width containers -->
<div class="container mx-auto px-4">
<div class="max-w-[1120px] w-full mx-auto">
```

### Grid Layouts
```html
<!-- Two-column responsive layout -->
<div class="grid lg:grid-cols-2 gap-8 items-center">

<!-- Three-column responsive layout -->
<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">

<!-- Article/Card grid -->
<div class="flex flex-col md:flex-row md:justify-center gap-6">
```

## 🎯 Section Structure Pattern

### Standard Section Header
```html
<section id="SectionName" class="[background-classes] [spacing-classes]">
  <div class="auto-container">
    <div class="flex flex-col items-center">
      <div class="sideline_text [color-class]">Section Label</div>
      <h1 class="text-4xl [alignment] [color-class]">Section Title</h1>
    </div>
    
    <div class="flex justify-center mt-3 mb-4">
      <div class="Nrule"></div>
      <div class="Nrule2"></div>
    </div>
    
    <!-- Section Content -->
  </div>
</section>
```

## 🎨 Background Patterns

### Section Background Classes
1. **Light Neutral**: `bg-white` or `bg-base-100`
2. **Primary Tint**: `bg-primary/10` or `bg-primary/20`
3. **Dark Cream**: `bg-dark-cream`
4. **Image Overlay**: 
   ```html
   <section class="relative bg-cover bg-top" style="background-image: url(...)">
     <div class="absolute inset-0 bg-primary opacity-85"></div>
     <div class="relative z-10"><!-- Content --></div>
   </section>
   ```

## 🃏 Card Design Patterns

### Standard Card
```html
<div class="bg-base-100 rounded-xl shadow-lg p-4">
  <!-- Card content -->
</div>
```

### Enhanced Card (Vision/Mission style)
```html
<div class="relative bg-base-100 text-black p-5 rounded-2xl shadow-lg max-w-md">
  <img class="absolute top-1/2 -left-2 transform -translate-y-1/2 w-16 h-16" src="icon.svg">
  <div class="pl-10">
    <!-- Content -->
  </div>
</div>
```

### Profile Cards (Management/Teachers)
```html
<div class="h-82 rounded-xl shadow-lg my-10 relative bg-white flex flex-col items-center p-0">
  <div class="rounded-t-xl h-42 w-full bg-secondary mb-4"></div>
  <div class="absolute top-[10%] left-1/2 transform -translate-x-1/2 w-30 h-30 flex justify-center items-center rounded-full border-4 border-white mb-3">
    <!-- Profile image or placeholder -->
  </div>
  <!-- Profile details -->
</div>
```

## 📏 Spacing System

### Section Spacing
- **Vertical padding**: `py-8`, `py-10`, `py-20`
- **Horizontal padding**: `px-2`, `px-4`, `px-[2vw]`, `px-[6.5vw]`
- **Margins**: `mt-4`, `mb-20`, `my-12`

### Content Spacing
- **Grid gaps**: `gap-4`, `gap-6`, `gap-8`
- **Space between**: `space-x-4`, `space-y-6`
- **Internal padding**: `p-4`, `p-5`, `p-10`

## 🎭 Typography Patterns

### Heading Hierarchy
```html
<div class="sideline_text [color]">Small Label</div>
<h1 class="text-4xl [color] [alignment]">Main Title</h1>
<h5 class="text-xl font-bold [color]">Subtitle</h5>
<h6 class="font-bold text-[13px]">Small Heading</h6>
```

### Text Styles
- **Body text**: Default or `text-sm`
- **Bold text**: `font-bold` or `font-medium`
- **Small text**: `text-[13px]`, `text-[8.25px]`

## 🔘 Button Patterns

### Primary Buttons
```html
<button class="btn btn-primary">Primary Action</button>
<a href="#" class="bg-primary text-white px-6 py-2 rounded font-medium hover:bg-opacity-90 transition-colors">Custom Primary</a>
```

### Secondary Buttons
```html
<button class="btn btn-secondary">Secondary Action</button>
```

## 🎠 Slider/Swiper Patterns

### Standard Swiper Setup
```html
<div class="max-w-[1120px] w-full mx-auto swiper">
  <div class="mx-2 md:mx-10 pb-5 rounded-3xl overflow-hidden slider-content">
    <div class="swiper-wrapper">
      <!-- Slides -->
    </div>
    <div class="swiper-button-next !text-primary !right-0 font-bold"></div>
    <div class="swiper-button-prev !text-primary !left-0 font-bold"></div>
    <div class="swiper-pagination [custom-pagination-class]"></div>
  </div>
</div>
```

## 🖼️ Image Patterns

### Responsive Images
```html
<img class="w-full h-48 object-cover rounded-t-xl" src="..." alt="...">
<img class="w-4/5 min-w-[250px] h-auto" src="..." alt="...">
```

### Profile Images
```html
<img class="w-24 h-24 object-cover object-top rounded-full" src="..." alt="...">
```

### Gallery Images
```html
<img class="h-48 w-auto object-cover rounded border border-gray-200 shadow-sm hover:shadow-md transition-shadow" src="..." alt="...">
```

## 🎪 Interactive Elements

### DaisyUI Dropdown
```html
<div class="dropdown">
  <div tabindex="0" role="button" class="btn btn-primary">
    Dropdown Text
    <svg><!-- Arrow icon --></svg>
  </div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-52 p-2 shadow">
    <!-- Menu items -->
  </ul>
</div>
```

### DaisyUI Accordion
```html
<div class="collapse collapse-plus bg-base-200 mb-2">
  <input type="radio" name="accordion-group" />
  <div class="collapse-title text-xl font-medium">Question</div>
  <div class="collapse-content">
    <p>Answer</p>
  </div>
</div>
```

## 🔄 State Patterns

### Empty States
```html
<div class="w-full">
  <div class="mx-auto max-w-[450px] max-h-[180px] bg-primary/20 py-20 px-12 text-primary">
    <h5 class="text-center">No [content] yet!</h5>
  </div>
</div>
```

### Loading/Placeholder States
```html
<div class="w-[150px] h-[180px] bg-secondary rounded-xl hidden sm:flex justify-center items-center">
  <i class="fa-solid fa-image text-4xl text-primary"></i>
</div>
```

## 📱 Responsive Patterns

### Visibility Classes
- **Hide on mobile**: `hidden md:block`, `hidden sm:block`
- **Show on mobile only**: `md:hidden`
- **Responsive grids**: `grid-cols-1 sm:grid-cols-2 md:grid-cols-3`

### Responsive Spacing
- **Responsive padding**: `px-2 md:px-10`, `py-8 md:py-12`
- **Responsive text**: `text-sm md:text-base`

## 🎨 Shadow System

### Card Shadows
- **Standard**: `shadow-lg`
- **Custom**: `shadow-card` (defined in CSS)
- **Subtle**: `shadow-sm`
- **Hover effects**: `hover:shadow-md transition-shadow`

## 🔧 Custom CSS Classes

### Decorative Elements
- `.Nrule` and `.Nrule2` - Custom rule decorations
- `.hr` - Custom horizontal rule
- `.sideline_text` - Small descriptive text style

### Layout Helpers
- `.auto-container` - Custom responsive container
- Custom font families via CSS variables

## 🎯 Form Patterns

### DaisyUI Form Controls
```html
<div class="form-control mb-12">
  <label class="label">
    <span class="label-text font-semibold text-primary">Label</span>
  </label>
  <input type="text" class="input placeholder:text-secondary focus:outline-orange focus:border-orange focus-within:outline-orange focus-within:border-orange w-full" placeholder="Placeholder" required />
</div>

<div class="form-control mb-12">
  <label class="label">
    <span class="label-text font-semibold text-[#052640]">Message</span>
  </label>
  <textarea class="textarea placeholder:text-secondary focus:outline-orange focus:border-orange focus-within:outline-orange focus-within:border-orange w-full h-24" rows="6" required></textarea>
</div>
```

## 🎪 Animation & Transitions

### Common Transitions
- **Hover effects**: `hover:bg-opacity-90 transition-colors`
- **Shadow transitions**: `hover:shadow-md transition-shadow`
- **Transform effects**: `transform -translate-x-1/2`, `transform -translate-y-1/2`

## 📐 Positioning Patterns

### Absolute Positioning
- **Centered**: `absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2`
- **Corner positioning**: `absolute top-[10%] left-1/2 transform -translate-x-1/2`
- **Decorative elements**: `absolute w-48 top-[7%] left-[3%]`

## 🎨 Design Principles

1. **Consistency**: Use the same spacing, colors, and patterns across all sections
2. **Hierarchy**: Clear visual hierarchy with typography and spacing
3. **Responsiveness**: Mobile-first approach with progressive enhancement
4. **Accessibility**: Proper semantic HTML and ARIA attributes
5. **Performance**: Optimized images and efficient CSS classes
6. **Maintainability**: Use of CSS variables and consistent naming

## 🔗 Integration Notes

- All colors are defined in the DaisyUI theme configuration
- Custom CSS variables are preserved for complex styling
- TailwindCSS utilities are preferred over custom CSS
- Component-based approach with reusable patterns
- Swiper.js integration for interactive carousels
- Font Awesome for icons throughout the design

This design system ensures consistency, maintainability, and scalability across the entire SMSS school website project.
