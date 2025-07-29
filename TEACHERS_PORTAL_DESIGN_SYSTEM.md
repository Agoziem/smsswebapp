# Teachers Portal Design System

## Overview
This design system defines the standardized patterns, components, and styling conventions for the Teachers Portal section of the SMSS website. It extends the main design system with teacher-specific elements and layouts.

## Color Palette

### Primary Colors
- **Primary Wine Red**: `#3b0505` (primary class)
- **Primary Light**: `primary/10`, `primary/5` for backgrounds
- **Primary Text**: Full opacity for headings, 60% opacity for labels

### Semantic Colors
- **Success Green**: `green-600`, `green-400` for positive actions
- **Info Blue**: `info` class for informational elements  
- **Warning Orange**: `warning` for alerts and attention
- **Error Red**: `error` for destructive actions

### Background Colors
- **Page Background**: `bg-primary/10` (light wine tint)
- **Card Background**: `bg-base-100` (white/neutral)
- **Hover States**: `bg-base-200/50`, `bg-base-200`
- **Section Backgrounds**: `bg-base-200/50` for activity items

## Layout Structure

### Dashboard Layout
```
Main Container: min-h-screen flex flex-col
├── Drawer System: drawer lg:drawer-open
│   ├── Sidebar: Fixed navigation with teacher-specific links
│   └── Main Content: drawer-content flex flex-col min-h-screen
│       ├── Navbar: Sticky top navigation with search
│       ├── Main: flex-grow bg-primary/10 p-6
│       └── Footer: Consistent footer component
```

### Grid Systems
- **Statistics Cards**: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6`
- **Dashboard Layout**: `grid lg:grid-cols-12 gap-8`
  - Content Area: `lg:col-span-8`
  - Sidebar Content: `lg:col-span-4`
- **Quick Actions**: `grid grid-cols-2 md:grid-cols-4 gap-4`

## Typography

### Headings
- **Page Title**: `text-2xl md:text-3xl font-bold text-primary`
- **Section Headers**: `text-lg font-bold text-primary`
- **Card Titles**: `text-sm text-{color}/60 font-medium` (labels)
- **Statistics**: `text-3xl font-bold text-{color}`

### Body Text
- **Descriptions**: `text-sm text-base-content/70`
- **Activity Text**: `text-sm font-medium text-base-content`
- **Timestamps**: `text-xs text-base-content/60`

## Component Patterns

### Statistics Cards
```html
<div class="bg-base-100 rounded-xl shadow-lg p-6 border-l-4 border-{color}">
  <div class="flex items-center justify-between">
    <div>
      <p class="text-sm text-{color}/60 font-medium">{Label}</p>
      <p class="text-3xl font-bold text-{color}">{Value}</p>
      <p class="text-xs text-{color} mt-1">
        <i class="fas fa-arrow-up mr-1"></i>{Status}
      </p>
    </div>
    <div class="bg-{color}/10 p-4 rounded-full">
      <i class="fas {icon} text-{color} text-2xl"></i>
    </div>
  </div>
</div>
```

### Quick Action Cards
```html
<a href="#" class="group bg-{color}/5 hover:bg-{color} hover:text-white transition-all duration-300 rounded-xl p-4 text-center border border-{color}">
  <div class="bg-{color}/10 group-hover:bg-white/20 p-3 rounded-full w-12 h-12 flex justify-center items-center mx-auto mb-3">
    <i class="fas {icon} text-{color} group-hover:text-white text-xl"></i>
  </div>
  <p class="text-sm font-medium text-{color} group-hover:text-white">{Label}</p>
</a>
```

### Activity Items
```html
<div class="flex items-start gap-4 py-4 bg-base-200/50 rounded-lg hover:bg-base-200 transition-colors">
  <div class="bg-{type}/10 p-2 rounded-full flex-shrink-0 w-10 h-10 flex items-center justify-center">
    <i class="fas {icon} text-{type} text-sm"></i>
  </div>
  <div class="flex-grow">
    <p class="text-sm font-medium text-base-content">{description}</p>
    <p class="text-xs text-base-content/60 mt-1">{timestamp}</p>
  </div>
  <div class="badge badge-{type} badge-outline badge-sm">{category}</div>
</div>
```

### Data Table Cards
```html
<div class="bg-base-100 rounded-xl shadow-lg p-6 mb-8 space-y-4 w-[85vw] md:w-full mx-auto">
  <!-- Header -->
  <div class="mb-6">
    <h6 class="text-lg font-bold text-primary">{Title}</h6>
    <p class="text-sm text-base-content/70">{Description}</p>
  </div>
  
  <!-- Controls -->
  <!-- Table -->
  <!-- Pagination -->
</div>
```

## Interactive Elements

### Form Controls
- **Input Fields**: `input input-bordered placeholder:text-secondary focus:outline-orange focus:border-orange`
- **Select Dropdowns**: `select select-bordered placeholder:text-secondary focus:outline-orange focus:border-orange`
- **Search Groups**: `h-[35px] rounded-md` for consistent height
- **Button Heights**: `h-[35px]` to match inputs

### Buttons
- **Primary Actions**: `btn btn-primary`
- **Secondary Actions**: `btn btn-secondary`
- **Success Actions**: `btn btn-success`
- **Warning Actions**: `btn btn-warning`
- **Error Actions**: `btn btn-error`
- **Small Buttons**: Add `btn-sm` class
- **Icon Buttons**: `btn btn-square` for square buttons

### Navigation
- **Badges**: `badge badge-{color} badge-outline badge-sm`
- **Links**: `link link-hover underline` for text links

## Spacing System

### Margins & Padding
- **Page Padding**: `p-6` for main content areas
- **Card Padding**: `p-6` for card containers
- **Section Spacing**: `mb-8` between major sections
- **Component Spacing**: `mb-6` between components
- **Element Spacing**: `space-y-4` for vertical stacking
- **Grid Gaps**: `gap-6` for cards, `gap-8` for sections, `gap-4` for actions

### Container Widths
- **Mobile Responsive**: `w-[85vw] md:w-full mx-auto` for cards
- **Form Elements**: `w-full max-w-xs` for inputs
- **Icon Containers**: `w-12 h-12` for action icons, `w-10 h-10` for activity icons

## Responsive Design

### Breakpoints
- **Mobile First**: Default mobile layout
- **Medium (md)**: Tablet adjustments
- **Large (lg)**: Desktop layouts with sidebar

### Mobile Considerations
- **Navigation**: Drawer toggle for mobile
- **Search**: Hidden on mobile, toggle button shown
- **Grid Adjustments**: Single column on mobile, multi-column on larger screens
- **Width Constraints**: `w-[85vw]` for mobile card containers

## Animation & Transitions

### Hover Effects
- **Duration**: `transition-all duration-300`
- **Color Transitions**: `transition-colors`
- **Background Changes**: Subtle opacity shifts
- **Group Hover**: Coordinated hover states for card elements

### Loading States
- **Skeleton Loading**: Use `animate-pulse` for loading states
- **Button Loading**: `loading loading-spinner` for async actions

## Accessibility

### ARIA Labels
- Proper labeling for interactive elements
- Screen reader friendly navigation

### Color Contrast
- Sufficient contrast ratios maintained
- Alternative indicators beyond color

### Keyboard Navigation
- Tab order consideration
- Focus states maintained

## Component Usage Guidelines

### When to Use Cards
- Grouping related content
- Creating visual hierarchy
- Containing interactive elements

### When to Use Grids
- Displaying statistics
- Organizing quick actions
- Responsive layouts

### Color Assignment
- **Primary (Wine Red)**: Main actions, primary content, branding
- **Green**: Success states, positive metrics, confirmations
- **Blue (Info)**: Informational content, secondary actions
- **Orange (Warning)**: Alerts, attention-required items
- **Red (Error)**: Destructive actions, errors, critical alerts

## Implementation Examples

### Page Header Pattern
```html
<div class="mb-8">
  <div class="space-y-2">
    <h1 class="text-2xl md:text-3xl font-bold text-primary">{Page Title}</h1>
    <!-- Status/Alert Components -->
  </div>
</div>
```

### Alert Pattern
```html
<div class="bg-{type}/10 border border-{type}/20 rounded-lg p-4 max-w-md">
  <div class="flex items-center gap-3">
    <i class="fas {icon} text-{type} text-lg"></i>
    <div>
      <p class="font-medium text-{type}">{Title}</p>
      <p class="text-sm text-{type}/80">{Message}</p>
    </div>
  </div>
</div>
```

### Statistics Grid Pattern
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
  <!-- Statistics cards with color coding -->
</div>
```

## File Organization

### Component Structure
```
_components/
├── stats_cards.html          # Dashboard statistics
├── quick_actions.html        # Action buttons grid
├── recent_activities.html    # Activity feed
├── students_table.html       # Data table component
├── class_students_table.html # Specialized table
├── dashboard_scripts.html    # JavaScript components
└── back_to_top.html         # Utility component
```

### Layout Structure
```
_layouts/
├── dashboard_layout.html     # Main layout wrapper
├── sidebar.html             # Navigation sidebar
├── navbar.html              # Top navigation
└── footer.html              # Footer component
```

## Best Practices

1. **Consistency**: Use established patterns across all teacher pages
2. **Responsiveness**: Ensure mobile-first design approach
3. **Performance**: Minimize CSS and maintain efficient DOM structure
4. **Accessibility**: Include proper ARIA labels and semantic HTML
5. **Modularity**: Keep components reusable and self-contained
6. **Color Usage**: Follow semantic color assignments consistently
7. **Spacing**: Use the established spacing system for visual rhythm
8. **Typography**: Maintain hierarchy with consistent font sizing
9. **Interactive States**: Include hover, focus, and active states
10. **Loading States**: Plan for async content and loading indicators

This design system should be referenced when updating other Teachers Portal pages to ensure consistency and maintainability across the entire teacher interface.
