/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./content/**/*.{md,mdx,html}",
    "./src/**/*.{html,njk,liquid,js}",
    "./src/_includes/**/*.{html,njk,liquid}",
    "./src/_layouts/**/*.{html,njk,liquid}"
  ],
  theme: {
    extend: {
      colors: {
        'ai-blue': {
          50: '#eff6ff',
          100: '#dbeafe', 
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a'
        },
        'ai-purple': {
          50: '#faf5ff',
          100: '#f3e8ff',
          200: '#e9d5ff', 
          300: '#d8b4fe',
          400: '#c084fc',
          500: '#a855f7',
          600: '#9333ea',
          700: '#7c3aed',
          800: '#6b21a8',
          900: '#581c87'
        }
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
        'mono': ['JetBrains Mono', 'monospace']
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: 'none',
            color: '#374151',
            '[class~="lead"]': {
              color: '#4b5563',
            },
            a: {
              color: '#3b82f6',
              textDecoration: 'underline',
              '&:hover': {
                color: '#1d4ed8',
              },
            },
            strong: {
              color: '#111827',
            },
            'ol > li::before': {
              color: '#6b7280',
            },
            'ul > li::before': {
              backgroundColor: '#d1d5db',
            },
            hr: {
              borderColor: '#e5e7eb',
            },
            blockquote: {
              color: '#374151',
              borderLeftColor: '#e5e7eb',
            },
            h1: {
              color: '#111827',
            },
            h2: {
              color: '#111827', 
            },
            h3: {
              color: '#111827',
            },
            h4: {
              color: '#111827',
            },
            'figure figcaption': {
              color: '#6b7280',
            },
            code: {
              color: '#111827',
            },
            'a code': {
              color: '#111827',
            },
            pre: {
              color: '#e5e7eb',
              backgroundColor: '#1f2937',
            },
            thead: {
              color: '#111827',
              borderBottomColor: '#d1d5db',
            },
            'tbody tr': {
              borderBottomColor: '#e5e7eb',
            },
          },
        },
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
} 