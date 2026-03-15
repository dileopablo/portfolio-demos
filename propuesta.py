from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import KeepTogether

W, H = A4

# ── COLORES ──
NEGRO     = colors.HexColor('#111111')
GRIS      = colors.HexColor('#555555')
GRIS_CLAR = colors.HexColor('#888888')
BORDE     = colors.HexColor('#e0e0e0')
FONDO     = colors.HexColor('#f8f8f8')
ACENTO    = colors.HexColor('#2271b1')
ACENTO2   = colors.HexColor('#e8f0fb')
VERDE     = colors.HexColor('#1a7a4a')
VERDE_CL  = colors.HexColor('#edfaef')
NARANJA   = colors.HexColor('#c45000')
NARANJA_C = colors.HexColor('#fff3ec')
NEGRO_HEA = colors.HexColor('#0a0a0a')

doc = SimpleDocTemplate(
    '/home/claude/propuesta_pablo.pdf',
    pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=14*mm, bottomMargin=14*mm,
)

# ── ESTILOS ──
styles = getSampleStyleSheet()

def est(name, parent='Normal', **kw):
    s = ParagraphStyle(name, parent=styles[parent], **kw)
    return s

TITULO_DOC  = est('TituloDoc',  fontSize=26, textColor=colors.white,   leading=30, fontName='Helvetica-Bold', spaceAfter=2)
SUBTITULO   = est('Subtitulo',  fontSize=11, textColor=colors.HexColor('#a0c4f0'), leading=14, fontName='Helvetica')
SECCION     = est('Seccion',    fontSize=13, textColor=ACENTO,  leading=16, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=6)
CUERPO      = est('Cuerpo',     fontSize=9.5, textColor=GRIS,   leading=14, fontName='Helvetica', spaceAfter=4)
CUERPO_NEG  = est('CuerpoNeg',  fontSize=9.5, textColor=NEGRO,  leading=14, fontName='Helvetica-Bold', spaceAfter=4)
SMALL       = est('Small',      fontSize=8.5, textColor=GRIS_CLAR, leading=12, fontName='Helvetica')
PRECIO      = est('Precio',     fontSize=18, textColor=ACENTO,  leading=22, fontName='Helvetica-Bold')
PRECIO_LBL  = est('PrecioLbl',  fontSize=8,  textColor=GRIS_CLAR, leading=10, fontName='Helvetica')
VIÑETA      = est('Vineta',     fontSize=9.5, textColor=GRIS,   leading=14, fontName='Helvetica', leftIndent=10, spaceAfter=3)
FOOTER_EST  = est('Footer',     fontSize=8,  textColor=GRIS_CLAR, leading=10, fontName='Helvetica', alignment=TA_CENTER)
TAG_TXT     = est('TagTxt',     fontSize=8,  textColor=ACENTO,  leading=10, fontName='Helvetica-Bold', alignment=TA_CENTER)
TAG_VERDE   = est('TagVerde',   fontSize=8,  textColor=VERDE,   leading=10, fontName='Helvetica-Bold', alignment=TA_CENTER)
TAG_NAR     = est('TagNar',     fontSize=8,  textColor=NARANJA, leading=10, fontName='Helvetica-Bold', alignment=TA_CENTER)
HIGHLIGHT   = est('Highlight',  fontSize=9.5, textColor=ACENTO, leading=14, fontName='Helvetica-Bold', spaceAfter=4)

story = []

# ══════════════════════════════════════════
# CABECERA
# ══════════════════════════════════════════
header_data = [[
    Paragraph('PROPUESTA COMERCIAL', TITULO_DOC),
    Paragraph('Pablo Dileo · Diseño Web<br/>Reconquista, Santa Fe<br/>+54 9 3482 257895', SUBTITULO),
]]
header_tbl = Table(header_data, colWidths=[110*mm, 64*mm])
header_tbl.setStyle(TableStyle([
    ('BACKGROUND',   (0,0), (-1,-1), NEGRO_HEA),
    ('VALIGN',       (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING',  (0,0), (0,0),   10*mm),
    ('RIGHTPADDING', (1,0), (1,0),   8*mm),
    ('TOPPADDING',   (0,0), (-1,-1), 8*mm),
    ('BOTTOMPADDING',(0,0), (-1,-1), 8*mm),
    ('ALIGN',        (1,0), (1,0),   'RIGHT'),
    ('ROUNDEDCORNERS', [4,4,4,4]),
]))
story.append(header_tbl)
story.append(Spacer(1, 6*mm))

# ══════════════════════════════════════════
# INTRO
# ══════════════════════════════════════════
story.append(Paragraph('¿Por qué tu negocio necesita una página web?', SECCION))
story.append(Paragraph(
    'Hoy cuando alguien busca un servicio en tu ciudad, lo primero que hace es buscarlo en Google. '
    'Si tu negocio no aparece, ese cliente se lo lleva la competencia. Una página web profesional '
    'te pone en los resultados de búsqueda, transmite confianza y trabaja por vos las 24 horas.',
    CUERPO
))
story.append(Spacer(1, 3*mm))

# Tres puntos destacados
puntos_data = [
    ['🔍  Aparecés en Google', '📱  Tus clientes te encuentran', '💬  Recibís consultas por WhatsApp'],
    [
        Paragraph('Cuando alguien busca tu rubro en tu ciudad, tu página aparece en los resultados.', SMALL),
        Paragraph('La página funciona 24hs. Tu cliente encuentra toda la info cuando la necesita.', SMALL),
        Paragraph('Botón directo a WhatsApp con el mensaje ya escrito. Sin fricción.', SMALL),
    ]
]
puntos_tbl = Table(puntos_data, colWidths=[57*mm, 57*mm, 57*mm])
puntos_tbl.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (-1,0),  ACENTO2),
    ('BACKGROUND',    (0,1), (-1,1),  colors.white),
    ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
    ('FONTSIZE',      (0,0), (-1,0),  9),
    ('TEXTCOLOR',     (0,0), (-1,0),  ACENTO),
    ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',    (0,0), (-1,0),  5*mm),
    ('BOTTOMPADDING', (0,0), (-1,0),  4*mm),
    ('TOPPADDING',    (0,1), (-1,1),  4*mm),
    ('BOTTOMPADDING', (0,1), (-1,1),  5*mm),
    ('LEFTPADDING',   (0,0), (-1,-1), 4*mm),
    ('RIGHTPADDING',  (0,0), (-1,-1), 4*mm),
    ('GRID',          (0,0), (-1,-1), 0.5, BORDE),
    ('ROUNDEDCORNERS', [4,4,4,4]),
]))
story.append(puntos_tbl)
story.append(Spacer(1, 5*mm))

# ══════════════════════════════════════════
# QUÉ INCLUYE
# ══════════════════════════════════════════
story.append(HRFlowable(width='100%', thickness=0.5, color=BORDE, spaceAfter=4*mm))
story.append(Paragraph('¿Qué incluye la página?', SECCION))

incluye = [
    ('🎨', 'Diseño profesional a medida', 'Con tu identidad, colores y contenido. No es una plantilla genérica.'),
    ('📱', 'Diseño responsivo', 'Se adapta a celular, tablet y computadora. Hoy el 70% de las visitas son desde el teléfono.'),
    ('🔍', 'Optimización SEO', 'Configuramos el título, descripción, palabras clave y datos estructurados para que Google te encuentre.'),
    ('💬', 'Botón de WhatsApp', 'Con mensaje pre-armado. El cliente hace clic y ya tiene el mensaje listo para enviar.'),
    ('📋', 'Formulario de contacto', 'Llega al correo del negocio o se puede conectar a Google Sheets para registrar consultas.'),
    ('🔒', 'SSL incluido', 'El candadito de seguridad. Sin SSL Google marca la página como "No seguro".'),
    ('🗺️', 'Google Maps integrado', 'El cliente puede ver dónde están y cómo llegar desde el celular.'),
    ('📰', 'Panel de noticias', 'Con WordPress el cliente puede publicar novedades sin saber programación.'),
]

for icono, titulo, desc in incluye:
    fila = Table([[
        Paragraph(icono, est('ic', fontSize=14, leading=16, alignment=TA_CENTER)),
        [Paragraph(f'<b>{titulo}</b>', CUERPO_NEG), Paragraph(desc, SMALL)]
    ]], colWidths=[10*mm, 161*mm])
    fila.setStyle(TableStyle([
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',   (0,0), (0,0),   0),
        ('RIGHTPADDING',  (0,0), (0,0),   3*mm),
        ('TOPPADDING',    (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(fila)
    story.append(Spacer(1, 2*mm))

story.append(Spacer(1, 3*mm))

# ══════════════════════════════════════════
# PRECIOS
# ══════════════════════════════════════════
story.append(HRFlowable(width='100%', thickness=0.5, color=BORDE, spaceAfter=4*mm))
story.append(Paragraph('Precios', SECCION))

# Tabla de precios
precio_header = [
    Paragraph('PLAN', est('ph', fontSize=9, textColor=colors.white, fontName='Helvetica-Bold', alignment=TA_CENTER)),
    Paragraph('QUÉ INCLUYE', est('ph', fontSize=9, textColor=colors.white, fontName='Helvetica-Bold', alignment=TA_CENTER)),
    Paragraph('PRECIO INICIAL', est('ph', fontSize=9, textColor=colors.white, fontName='Helvetica-Bold', alignment=TA_CENTER)),
    Paragraph('ABONO MENSUAL', est('ph', fontSize=9, textColor=colors.white, fontName='Helvetica-Bold', alignment=TA_CENTER)),
]

planes = [
    ('Básico', 'Barbería, servicio técnico, auxilio, negocio chico.\n4-6 secciones, formulario, WhatsApp, SEO.', 'desde\n$80.000', 'desde\n$15.000'),
    ('Estándar', 'Club, instituto, colegio profesional, comercio con catálogo.\n6-8 secciones + panel de noticias.', 'desde\n$150.000', 'desde\n$25.000'),
    ('Avanzado', 'Múltiples profesionales, buscador, sistema de reservas,\nfiltros dinámicos.', 'desde\n$300.000', 'desde\n$45.000'),
]

precio_rows = [precio_header]
for plan, incluye_txt, precio_i, precio_m in planes:
    precio_rows.append([
        Paragraph(f'<b>{plan}</b>', est('pn', fontSize=9.5, fontName='Helvetica-Bold', alignment=TA_CENTER, textColor=NEGRO)),
        Paragraph(incluye_txt.replace('\n','<br/>'), est('pd', fontSize=8.5, textColor=GRIS, leading=12)),
        Paragraph(precio_i.replace('\n','<br/>'), est('pp', fontSize=12, fontName='Helvetica-Bold', textColor=ACENTO, alignment=TA_CENTER, leading=16)),
        Paragraph(precio_m.replace('\n','<br/>'), est('pm', fontSize=11, fontName='Helvetica-Bold', textColor=VERDE, alignment=TA_CENTER, leading=15)),
    ])

precio_tbl = Table(precio_rows, colWidths=[28*mm, 80*mm, 30*mm, 34*mm])
precio_tbl.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (-1,0),  NEGRO_HEA),
    ('BACKGROUND',    (0,1), (-1,1),  colors.white),
    ('BACKGROUND',    (0,2), (-1,2),  FONDO),
    ('BACKGROUND',    (0,3), (-1,3),  colors.white),
    ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',    (0,0), (-1,-1), 4*mm),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4*mm),
    ('LEFTPADDING',   (0,0), (-1,-1), 3*mm),
    ('RIGHTPADDING',  (0,0), (-1,-1), 3*mm),
    ('GRID',          (0,0), (-1,-1), 0.5, BORDE),
    ('LINEBELOW',     (0,0), (-1,0),  1,   ACENTO),
]))
story.append(precio_tbl)

story.append(Spacer(1, 3*mm))
story.append(Paragraph(
    '* Los precios son orientativos. El presupuesto final depende de los requerimientos específicos del proyecto.',
    SMALL
))
story.append(Spacer(1, 4*mm))

# ══════════════════════════════════════════
# HOSTING Y DOMINIO
# ══════════════════════════════════════════
story.append(HRFlowable(width='100%', thickness=0.5, color=BORDE, spaceAfter=4*mm))
story.append(Paragraph('Hosting y dominio', SECCION))
story.append(Paragraph(
    'Para que tu página esté visible en internet necesitás dos cosas: un <b>dominio</b> '
    '(tu dirección web, como <i>tunegocio.com.ar</i>) y un <b>hosting</b> (el servidor donde vive la página). '
    'Ambos tienen un costo pequeño que se gestiona de forma transparente y se incluye dentro del abono mensual '
    'de mantenimiento — vos no tenés que preocuparte por nada técnico.',
    CUERPO
))
story.append(Spacer(1, 2*mm))

hosting_simple = [[
    Paragraph('🌐  Dominio (.com.ar o .com)', est('hs', fontSize=9, fontName='Helvetica-Bold', textColor=ACENTO)),
    Paragraph('🖥️  Hosting (servidor)', est('hs', fontSize=9, fontName='Helvetica-Bold', textColor=ACENTO)),
    Paragraph('🔒  SSL (seguridad)', est('hs', fontSize=9, fontName='Helvetica-Bold', textColor=ACENTO)),
],[
    Paragraph('Tu dirección en internet.\nRenovación anual incluida.', SMALL),
    Paragraph('Donde vive tu página.\nIncluido en el abono mensual.', SMALL),
    Paragraph('El candadito de seguridad.\nRequerido por Google. Incluido.', SMALL),
]]
hs_tbl = Table(hosting_simple, colWidths=[57*mm, 57*mm, 57*mm])
hs_tbl.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (-1,0),  ACENTO2),
    ('BACKGROUND',    (0,1), (-1,1),  colors.white),
    ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',    (0,0), (-1,-1), 4*mm),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4*mm),
    ('LEFTPADDING',   (0,0), (-1,-1), 3*mm),
    ('RIGHTPADDING',  (0,0), (-1,-1), 3*mm),
    ('GRID',          (0,0), (-1,-1), 0.5, BORDE),
]))
story.append(hs_tbl)
story.append(Spacer(1, 4*mm))

# ══════════════════════════════════════════
# PROCESO DE TRABAJO
# ══════════════════════════════════════════
story.append(HRFlowable(width='100%', thickness=0.5, color=BORDE, spaceAfter=4*mm))
story.append(Paragraph('¿Cómo es el proceso?', SECCION))

pasos = [
    ('01', 'Reunión inicial',      'Charlamos sobre tu negocio, qué necesitás y cómo querés que se vea la página. Presupuesto sin cargo.'),
    ('02', 'Diseño y desarrollo',  'Armamos la página con tu información, fotos y contenido. Te mostramos avances para que apruebes.'),
    ('03', 'Revisión y ajustes',   'Hacemos los cambios que necesitás. Incluye hasta 2 rondas de revisiones sin costo adicional.'),
    ('04', 'Publicación',          'Subimos la página al hosting, configuramos el dominio, el SSL y verificamos que todo funcione.'),
    ('05', 'Entrega y capacitación','Te explicamos cómo actualizar contenido desde WordPress. Te dejamos todo funcionando.'),
]

pasos_data = [[
    Paragraph(f'<b>{num}</b>', est('pnum', fontSize=14, fontName='Helvetica-Bold', textColor=colors.white, alignment=TA_CENTER)),
    [Paragraph(f'<b>{tit}</b>', CUERPO_NEG), Paragraph(desc, SMALL)]
] for num, tit, desc in pasos]

pasos_tbl = Table(pasos_data, colWidths=[12*mm, 159*mm])
pasos_tbl.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (0,-1), ACENTO),
    ('ALIGN',         (0,0), (0,-1), 'CENTER'),
    ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',    (0,0), (-1,-1), 4*mm),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4*mm),
    ('LEFTPADDING',   (1,0), (1,-1), 5*mm),
    ('LINEBELOW',     (0,0), (-1,-2), 0.5, BORDE),
]))
story.append(pasos_tbl)
story.append(Spacer(1, 4*mm))

# ══════════════════════════════════════════
# TIPOS DE NEGOCIOS
# ══════════════════════════════════════════
story.append(HRFlowable(width='100%', thickness=0.5, color=BORDE, spaceAfter=4*mm))
story.append(Paragraph('Tipos de negocios que atendemos', SECCION))

negocios = [
    '🏋️ Gimnasios y centros deportivos',    '💈 Barberías y peluquerías',
    '🏫 Institutos educativos',              '⚽ Clubes deportivos',
    '🏗️ Servicios de construcción',          '❄️ Servicios técnicos',
    '🚨 Servicios de auxilio en ruta',       '👨‍🏫 Profesores y tutores',
    '🏢 Colegios y asociaciones profesionales', '🌿 Emprendimientos y comercios',
]

neg_rows = []
for i in range(0, len(negocios), 2):
    neg_rows.append([
        Paragraph(negocios[i], est('neg', fontSize=9, textColor=GRIS, leading=13)),
        Paragraph(negocios[i+1] if i+1 < len(negocios) else '', est('neg', fontSize=9, textColor=GRIS, leading=13)),
    ])

neg_tbl = Table(neg_rows, colWidths=[86*mm, 86*mm])
neg_tbl.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (-1,-1), FONDO),
    ('TOPPADDING',    (0,0), (-1,-1), 3*mm),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3*mm),
    ('LEFTPADDING',   (0,0), (-1,-1), 4*mm),
    ('GRID',          (0,0), (-1,-1), 0.5, BORDE),
]))
story.append(neg_tbl)
story.append(Spacer(1, 4*mm))

# ══════════════════════════════════════════
# GARANTÍAS
# ══════════════════════════════════════════
story.append(HRFlowable(width='100%', thickness=0.5, color=BORDE, spaceAfter=4*mm))
story.append(Paragraph('Lo que garantizamos', SECCION))

garantias = [
    ('✅', 'Diseño exclusivo',      'Cada página es única, adaptada a tu negocio. No usamos plantillas genéricas.'),
    ('✅', 'SEO incluido',          'Optimización para Google desde el primer día. Título, descripción, Schema.org y más.'),
    ('✅', 'Soporte mensual',       'Ante cualquier problema técnico te respondemos y solucionamos. Siempre disponibles.'),
    ('✅', 'Primer mes gratis',     'El primer mes de abono de mantenimiento es sin cargo para nuevos clientes.'),
    ('✅', 'Sin contratos largos',  'El abono mensual se puede cancelar en cualquier momento. Sin letra chica.'),
]

for icono, tit, desc in garantias:
    g = Table([[
        Paragraph(icono, est('gi', fontSize=12, leading=14, alignment=TA_CENTER)),
        [Paragraph(f'<b>{tit}</b>', CUERPO_NEG), Paragraph(desc, SMALL)]
    ]], colWidths=[10*mm, 161*mm])
    g.setStyle(TableStyle([
        ('VALIGN',  (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0),(0,0), 0),
        ('RIGHTPADDING',(0,0),(0,0), 3*mm),
        ('TOPPADDING',  (0,0),(-1,-1), 2),
        ('BOTTOMPADDING',(0,0),(-1,-1), 2),
    ]))
    story.append(g)
    story.append(Spacer(1, 2*mm))

story.append(Spacer(1, 4*mm))

# ══════════════════════════════════════════
# CTA FINAL
# ══════════════════════════════════════════
cta_data = [[
    Paragraph('¿Listo para tener tu página web?', est('ctah', fontSize=14, fontName='Helvetica-Bold', textColor=colors.white, alignment=TA_CENTER)),
],[
    Paragraph(
        'Escribime por WhatsApp o llamame para coordinar una reunión sin cargo.<br/>'
        'Te muestro ejemplos reales y armamos juntos lo que tu negocio necesita.',
        est('ctab', fontSize=10, textColor=colors.HexColor('#c0d8f5'), alignment=TA_CENTER, leading=15)
    ),
],[
    Paragraph(
        '📱  +54 9 3482 257895  ·  Pablo Dileo  ·  Reconquista, Santa Fe',
        est('ctac', fontSize=10, fontName='Helvetica-Bold', textColor=colors.white, alignment=TA_CENTER)
    ),
]]

cta_tbl = Table(cta_data, colWidths=[172*mm])
cta_tbl.setStyle(TableStyle([
    ('BACKGROUND',    (0,0), (-1,-1), NEGRO_HEA),
    ('TOPPADDING',    (0,0), (-1,-1), 5*mm),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5*mm),
    ('LEFTPADDING',   (0,0), (-1,-1), 8*mm),
    ('RIGHTPADDING',  (0,0), (-1,-1), 8*mm),
    ('LINEABOVE',     (0,0), (-1,0),  3, ACENTO),
    ('ROUNDEDCORNERS', [4,4,4,4]),
]))
story.append(cta_tbl)
story.append(Spacer(1, 4*mm))

# FOOTER
story.append(HRFlowable(width='100%', thickness=0.5, color=BORDE, spaceAfter=3*mm))
story.append(Paragraph(
    'Pablo Dileo · Diseño web profesional · Reconquista, Santa Fe · 2026<br/>'
    'Este documento es una propuesta comercial orientativa. Los precios finales se acuerdan según los requerimientos de cada proyecto.',
    FOOTER_EST
))

doc.build(story)
print("PDF generado correctamente")
