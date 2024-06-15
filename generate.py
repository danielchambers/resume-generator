from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, Table, TableStyle, Flowable

data = {
    "filename": "resume.pdf",
    "margins": {
        "leftMargin": 15,
        "rightMargin": 15,
        "topMargin": 15,
        "bottomMargin": 15,
    },
    "font": "Helvetica",
    "font_size": 10,
    "title_size": 12,
    "sections": {
        "personal_info": {
            "name": "John Doe",
            "location": "Los Angeles, California",
            "email": "email@johndoe.com",
            "phone": "+1 514-456-7890",
            "website": "johndoe.com",
            "github": "github.com/johndoe",
            "linkedin": "linkedin.com/in/johndoe",
        },
        # "summary": "Experienced software engineer with expertise in Python and web development.",
        "projects": [
            {
                "title": "Project 1",
                "role": "Developer",
                "link": "https://github.com/danielchambers/project1",
                "responsibilities": [
                    "Developed and maintained web applications using Python and Django. The applications were used by over 100,000 users.",
                    "Collaborated with cross-functional teams to deliver high-quality software. Worked closely with product managers, designers, and other engineers."
                ],
            },
            {
                "title": "Project 2",
                "role": "Developer",
                "link": "https://github.com/danielchambers/project2",
                "responsibilities": [
                    "Developed and maintained web applications using Python and Django. The applications were used by over 100,000 users.",
                    "Collaborated with cross-functional teams to deliver high-quality software. Worked closely with product managers, designers, and other engineers."
                ],
            },
            {
                "title": "Project 3",
                "role": "Developer",
                "link": "https://github.com/danielchambers/project3",
                "responsibilities": [
                    "Developed and maintained web applications using Python and Django. The applications were used by over 100,000 users.",
                    "Collaborated with cross-functional teams to deliver high-quality software. Worked closely with product managers, designers, and other engineers."
                ],
            },
        ],
        "experience": [
            {
                "title": "Software Engineer",
                "company": "ABC Company",
                "location": "Los Angeles, CA",
                "dates": "09/2018 - Present",
                "responsibilities": [
                    "Developed and maintained web applications using Python and Django. The applications were used by over 100,000 users.",
                    "Collaborated with cross-functional teams to deliver high-quality software. Worked closely with product managers, designers, and other engineers.",
                    "Implemented RESTful APIs for integration with external systems. The APIs were used by third-party developers to build applications on top of our platform.",
                ],
            },
            {
                "title": "Junior Software Developer",
                "company": "XYZ Corporation",
                "location": "Santa Monica, CA",
                "dates": "01/2016 - 08/2018",
                "responsibilities": [
                    "Assisted in the development of desktop applications using Python and PyQt. The applications were used by internal teams to automate business processes.",
                    "Conducted code reviews and resolved bugs and issues. Improved the quality and performance of the software.",
                    "Participated in agile development processes. Worked in sprints to deliver features and enhancements to the software.",
                ],
            },
        ],
        "education": [
            {
                "degree": "Bachelor of Science in Cognitive Science",
                "school": "University of California, Los Angeles",
                "location": "Los Angeles, CA",
                "dates": "09/2012 - 06/2016",
                "awards": "Deans List 2021",
                "relevant_courses": ["Introduction to Computer Science", "Data Structures and Algorithms", "Web Development", "Machine Learning"]
            },
            {
                "degree": "Associate of Science in Computer Science",
                "school": "Santa Monica City College",
                "location": "Santa Monica, CA",
                "dates": "09/2008 - 06/2012",
                "relevant_courses": ["Programming Fundamentals", "Database Management", "Software Engineering", "Operating Systems", "Computer Networks", "Computer Architecture", "Software Development"]
            },
        ],
        "skills": ["Python", "Django", "Flask", "JavaScript", "React", "HTML", "CSS", "SQL", "Git", "RESTful APIs", "Agile Development", "Code Reviews", "C++", "Java", "Ruby", "PHP", "Node.js", "Express", "MongoDB", "PostgreSQL", "SQLite", "Git", "GitHub", "GitLab", "Bitbucket", "JIRA", "Confluence", "C#"],
    },
}

class LineUnderTitle(Flowable):
    def __init__(self, width):
        Flowable.__init__(self)
        self.width = width

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColorRGB(0, 0, 0)
        self.canv.setLineWidth(1)
        self.canv.line(0, 0, self.width, 0)
        self.canv.restoreState()

def create_resume(data):
    doc = SimpleDocTemplate(
        data['filename'],
        pagesize=letter,
        rightMargin=data['margins']['rightMargin'],
        leftMargin=data['margins']['leftMargin'],
        topMargin=data['margins']['topMargin'],
        bottomMargin=data['margins']['bottomMargin']
    )

    elements = []
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    right_align_style = ParagraphStyle('RightAlign', parent=normal_style, alignment=2)

    # Add personal info
    personal_info = data['sections']['personal_info']
    name_style = ParagraphStyle(name='NameStyle', fontSize=18, spaceAfter=10, leading=14)
    elements.append(Paragraph(personal_info['name'], name_style))
    elements.append(Paragraph(f"{personal_info['location']}&nbsp;&nbsp;•&nbsp;&nbsp;{personal_info['email']}&nbsp;&nbsp;•&nbsp;&nbsp;{personal_info['phone']}", normal_style))
    elements.append(Paragraph(f'<a href="https://{personal_info['website']}">https://{personal_info['website']}</a>&nbsp;&nbsp;•&nbsp;&nbsp; <a href="https://{personal_info['github']}">https://{personal_info['github']}</a>&nbsp;&nbsp;•&nbsp;&nbsp; <a href="https://{personal_info['linkedin']}">https://{personal_info['linkedin']}</a>', normal_style))
    elements.append(Spacer(1, 12))

    # Add summary
    if 'summary' in data['sections']:
        elements.append(Paragraph("Summary", ParagraphStyle(name='Heading2', fontSize=data['title_size'], spaceAfter=6, leading=14)))
        elements.append(LineUnderTitle(doc.width))
        elements.append(Spacer(1, 6))
        elements.append(Paragraph(data['sections']['summary'], normal_style))
        elements.append(Spacer(1, 12))

    # Add skills
    elements.append(Paragraph("SKILLS", ParagraphStyle(name='Heading2', fontSize=data['title_size'], spaceAfter=2, leading=14)))
    elements.append(LineUnderTitle(doc.width))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(", ".join(data['sections']['skills']), normal_style))

    # Add projects
    elements.append(Paragraph("PROJECTS", ParagraphStyle(name='Heading2', fontSize=data['title_size'], spaceAfter=2, leading=14, spaceBefore=8)))
    elements.append(LineUnderTitle(doc.width))
    elements.append(Spacer(1, 6))
    for project in data['sections']['projects']:
        elements.append(Paragraph(f"{project['title']} - {project['role']}", ParagraphStyle(name='Heading3', fontSize=data['font_size'], leading=12, spaceBefore=1, spaceAfter=6, fontName='Helvetica-Bold')))
        elements.append(Paragraph(f'<a href="{project["link"]}">{project["link"]}</a>', normal_style))
        elements.append(ListFlowable([ListItem(Paragraph(resp, normal_style)) for resp in project['responsibilities']], bulletType='bullet'))
        elements.append(Spacer(1, 5))

    # Add experience
    elements.append(Paragraph("WORK EXPERIENCE", ParagraphStyle(name='Heading2', fontSize=data['title_size'], spaceAfter=2, leading=14, spaceBefore=8)))
    elements.append(LineUnderTitle(doc.width))
    elements.append(Spacer(1, 6))
    for job in data['sections']['experience']:
        elements.append(Paragraph(f"{job['title']}", ParagraphStyle(name='Heading3', fontSize=data['font_size'], leading=12, spaceBefore=1, spaceAfter=6, fontName='Helvetica-Bold')))
        
        # Create table for company, location, and dates
        exp_table = Table([
            [Paragraph(f"{job['company']}", normal_style), Paragraph(f"{job['location']} • {job['dates']}", right_align_style)]
        ], colWidths=[3.75 * inch, 4.20 * inch])
        exp_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (1, 0), 'TOP'),
        ]))
        elements.append(exp_table)

        elements.append(ListFlowable([ListItem(Paragraph(resp, normal_style)) for resp in job['responsibilities']], bulletType='bullet'))
        elements.append(Spacer(1, 5))

    # Add education
    elements.append(Paragraph("EDUCATION", ParagraphStyle(name='Heading2', fontSize=data['title_size'], spaceAfter=2, leading=14, spaceBefore=8)))
    elements.append(LineUnderTitle(doc.width))
    elements.append(Spacer(1, 6))
    for edu in data['sections']['education']:
        elements.append(Paragraph(f"{edu['degree']}", ParagraphStyle(name='Heading3', fontSize=data['font_size'], leading=12, spaceBefore=1, spaceAfter=6, fontName='Helvetica-Bold')))
        
        # Create table for school and dates
        edu_table = Table([
            [Paragraph(f"{edu['school']}", normal_style), Paragraph(f"{edu['location']} • {edu['dates']}", right_align_style)]
        ], colWidths=[3.75 * inch, 4.20 * inch])
        edu_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (1, 0), 'TOP'),
        ]))
        elements.append(edu_table)
        
        bullet_points = []
        if 'awards' in edu:
            bullet_points.append(ListItem(Paragraph(f"Awards: {edu['awards']}", normal_style)))
        if 'relevant_courses' in edu:
            bullet_points.append(ListItem(Paragraph(f"Relevant Courses: {', '.join(edu['relevant_courses'])}", normal_style)))
        
        if bullet_points:
            elements.append(ListFlowable(bullet_points, bulletType='bullet'))
        elements.append(Spacer(1, 5))

    doc.build(elements)

create_resume(data)
