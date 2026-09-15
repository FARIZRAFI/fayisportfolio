import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER

def generate_pdf():
    os.makedirs("assets", exist_ok=True)
    pdf_path = os.path.join("assets", "Muhammed_Fayis_CV.pdf")
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom engineering styles
    primary_color = HexColor("#0c1117")
    accent_blue = HexColor("#1e3a5f")
    steel_gray = HexColor("#475569")
    line_color = HexColor("#cbd5e1")
    dark_text = HexColor("#0f172a")
    
    name_style = ParagraphStyle(
        'Name',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        textTransform='uppercase'
    )
    
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=accent_blue,
        textTransform='uppercase'
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=steel_gray
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=15,
        textColor=accent_blue,
        spaceAfter=3,
        textTransform='uppercase'
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=dark_text
    )
    
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=steel_gray
    )
    
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=steel_gray,
        alignment=TA_RIGHT
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=dark_text
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=dark_text,
        leftIndent=12,
        firstLineIndent=-8
    )
    
    story = []
    
    # Header Table: Left (Name + Title) | Right (Contact Info)
    left_header = [
        Paragraph("<b>MUHAMMED FAYIS</b>", name_style),
        Paragraph("PROJECT PLANNING &amp; MANAGEMENT ENGINEER", title_style)
    ]
    
    right_header = [
        Paragraph("<b>Location:</b> Dammam, Eastern Province, Saudi Arabia", contact_style),
        Paragraph("<b>Email:</b> Muhdfayishere@gmail.com", contact_style),
        Paragraph("<b>Phone:</b> +966 596110525 / +966 507220185", contact_style),
        Paragraph("<b>Experience:</b> 5+ Years in Industrial &amp; Infrastructure Projects", contact_style)
    ]
    
    header_table = Table([[left_header, right_header]], colWidths=[310, 230])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent_blue, spaceBefore=4, spaceAfter=8))
    
    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    summary_text = (
        "Experienced Project Planning and Management Engineer with 5+ years of dedicated experience "
        "in project management, baseline planning, execution, and scheduling of large-scale structural steel fabrication, "
        "seawater desalination plants, and sewage water treatment plant (SWTP) projects. Proven expertise in "
        "multidisciplinary coordination, Primavera P6 scheduling, QA/QC documentation, change order management, "
        "resource allocation, delay impact analysis, and Extension of Time (EOT) claims."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.5, color=line_color, spaceBefore=2, spaceAfter=8))
    
    # Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_heading))
    
    # Role 1: BENA Steel Industries
    r1_left = [
        Paragraph("<b>PROJECT MANAGEMENT ENGINEER</b>", job_title_style),
        Paragraph("BENA Steel Industries &bull; Dammam, Saudi Arabia", company_style)
    ]
    r1_right = Paragraph("2025 &mdash; PRESENT", date_style)
    t1 = Table([[r1_left, r1_right]], colWidths=[420, 120])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t1)
    story.append(Paragraph("&bull; Overseeing end-to-end project management, fabrication scheduling, and site delivery for heavy structural steel and industrial infrastructure works.", bullet_style))
    story.append(Paragraph("&bull; Driving multidisciplinary engineering coordination across design, detailing, procurement, fabrication workshops, and site erection teams.", bullet_style))
    story.append(Paragraph("&bull; Tracking project milestones, resource leveling, risk matrices, and executive dashboard reporting to ensure on-schedule handover.", bullet_style))
    story.append(Paragraph("&bull; Enforcing rigorous QA/QC documentation compliance, ITP adherence, and industry safety standards across all active fabrication packages.", bullet_style))
    story.append(Spacer(1, 8))
    
    # Role 2: Acciona Agua
    r2_left = [
        Paragraph("<b>PLANNING ENGINEER</b>", job_title_style),
        Paragraph("Acciona Agua &bull; Saudi Arabia", company_style)
    ]
    r2_right = Paragraph("2024 &mdash; 2025", date_style)
    t2 = Table([[r2_left, r2_right]], colWidths=[420, 120])
    t2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t2)
    story.append(Paragraph("&bull; Developed and managed baseline project schedules in Primavera P6 for major desalination and water infrastructure utility installations.", bullet_style))
    story.append(Paragraph("&bull; Monitored Critical Path Method (CPM) activities, calculated schedule variances, and formulated proactive recovery strategies.", bullet_style))
    story.append(Paragraph("&bull; Formulated comprehensive daily, weekly, and monthly progress reports and S-curve analytical dashboards for executive stakeholders and clients.", bullet_style))
    story.append(Paragraph("&bull; Analyzed potential delays, assisted in preparing Extension of Time (EOT) claim justifications, and processed engineering change orders.", bullet_style))
    story.append(Spacer(1, 8))
    
    # Role 3: Wasalat Fabrications & Services
    r3_left = [
        Paragraph("<b>PROJECT ENGINEER</b>", job_title_style),
        Paragraph("Wasalat Fabrications &amp; Services &bull; Saudi Arabia", company_style)
    ]
    r3_right = Paragraph("2022 &mdash; 2024", date_style)
    t3 = Table([[r3_left, r3_right]], colWidths=[420, 120])
    t3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t3)
    story.append(Paragraph("&bull; Directed engineering operations, site fabrication, and mechanical erection across heavy industrial and utility plant facilities.", bullet_style))
    story.append(Paragraph("&bull; Monitored the fabrication and installation of <b>7,000+ Linear Meters (LM)</b> of pipelines for plant utilities and infrastructure facilities.", bullet_style))
    story.append(Paragraph("&bull; Coordinated subcontractor teams, verified material compliance, interpreted engineering drawings, and managed site variations.", bullet_style))
    story.append(Paragraph("&bull; Supervised QA/QC inspection routines, hydrostatic testing documentation, and non-conformance rectification.", bullet_style))
    story.append(Spacer(1, 8))
    
    # Role 4: Al Zayan Construction
    r4_left = [
        Paragraph("<b>SITE ENGINEER</b>", job_title_style),
        Paragraph("Al Zayan Construction &bull; Kerala, India", company_style)
    ]
    r4_right = Paragraph("2020 &mdash; 2021", date_style)
    t4 = Table([[r4_left, r4_right]], colWidths=[420, 120])
    t4.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t4)
    story.append(Paragraph("&bull; Supervised on-site construction works, structural execution, and technical alignment with structural and architectural drawings.", bullet_style))
    story.append(Paragraph("&bull; Handled subcontractor work allocations, daily material consumption logs, and site quality assurance inspections.", bullet_style))
    story.append(Paragraph("&bull; Enforced strict on-site occupational health and safety compliance standards.", bullet_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.5, color=line_color, spaceBefore=2, spaceAfter=8))
    
    # Core Skills & Competencies (Table 3 cols)
    story.append(Paragraph("TECHNICAL &amp; PROFESSIONAL COMPETENCIES", section_heading))
    col1 = [
        Paragraph("<b>PROJECT MANAGEMENT</b>", job_title_style),
        Paragraph("&bull; Primavera P6 Scheduling", bullet_style),
        Paragraph("&bull; MS Office Suite (Excel, Word, PPT)", bullet_style),
        Paragraph("&bull; Project Reporting &amp; Dashboards", bullet_style),
        Paragraph("&bull; Baseline Planning &amp; CPM Tracking", bullet_style),
        Paragraph("&bull; Change Orders &amp; EOT Claims", bullet_style)
    ]
    col2 = [
        Paragraph("<b>ENGINEERING &amp; CAD</b>", job_title_style),
        Paragraph("&bull; Navisworks Review &amp; Clash Check", bullet_style),
        Paragraph("&bull; AutoCAD (Basic Drawing Interpretation)", bullet_style),
        Paragraph("&bull; Technical Drawings Interpretation", bullet_style),
        Paragraph("&bull; Fabrication Shop Drawings Review", bullet_style),
        Paragraph("&bull; Multidisciplinary Coordination", bullet_style)
    ]
    col3 = [
        Paragraph("<b>QUALITY &amp; COMPLIANCE</b>", job_title_style),
        Paragraph("&bull; QA/QC Documentation &amp; ITPs", bullet_style),
        Paragraph("&bull; Safety Compliance (HSE Protocols)", bullet_style),
        Paragraph("&bull; Non-Conformance Reporting (NCR)", bullet_style),
        Paragraph("&bull; Subcontractor Management", bullet_style),
        Paragraph("&bull; Desalination &amp; SWTP Systems", bullet_style)
    ]
    skills_table = Table([[col1, col2, col3]], colWidths=[180, 180, 180])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.5, color=line_color, spaceBefore=2, spaceAfter=8))
    
    # Education & Languages
    story.append(Paragraph("EDUCATION, CERTIFICATIONS &amp; LANGUAGES", section_heading))
    
    edu_content = [
        Paragraph("<b>PROJECT MANAGEMENT PROFESSIONAL (PMP)&reg;</b> &bull; Global Credential<br/><font color='#475569'>Project Management Institute (PMI)&reg;</font>", body_style),
        Spacer(1, 4),
        Paragraph("<b>POST GRADUATE DIPLOMA IN QA/QC ENGINEERING</b> &bull; 2021 &ndash; 2022<br/><font color='#475569'>STED Council India</font>", body_style),
        Spacer(1, 4),
        Paragraph("<b>B.TECH IN MECHANICAL ENGINEERING</b> &bull; 2016 &ndash; 2020<br/><font color='#475569'>APJ Abdul Kalam Technological University, India</font>", body_style)
    ]
    
    lang_content = [
        Paragraph("<b>LANGUAGES</b>", job_title_style),
        Paragraph("&bull; English &mdash; Fluent", bullet_style),
        Paragraph("&bull; Hindi &mdash; Fluent", bullet_style),
        Paragraph("&bull; Malayalam &mdash; Fluent", bullet_style),
        Paragraph("&bull; Tamil &mdash; Fluent", bullet_style),
        Paragraph("&bull; Arabic &mdash; Basic", bullet_style)
    ]
    
    edu_lang_table = Table([[edu_content, lang_content]], colWidths=[340, 200])
    edu_lang_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_lang_table)
    
    doc.build(story)
    print(f"Successfully generated {pdf_path} ({os.path.getsize(pdf_path)} bytes)")

if __name__ == "__main__":
    generate_pdf()
