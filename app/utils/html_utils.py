def render_fibonacci_html(series: list[int], time_str: str) -> str:
    list_items = "\n".join(
        f'<li style="padding: 4px 0; border-bottom: 1px solid #eee;">{i+1}. <strong>{num}</strong></li>'
        for i, num in enumerate(series)
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <title>Serie Fibonacci</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: rgb(227, 232, 42);  /* Fondo con RGB */
          color: rgb(43, 55, 103);  /* Texto con RGB */
          padding: 20px;
        }}
        .container {{
          max-width: 600px;
          margin: 0 auto;
          background: #fff;
          border-radius: 8px;
          box-shadow: 0 2px 8px rgba(0,0,0,0.1);
          overflow: hidden;
        }}
        header {{
          background: #4CAF50;
          color: white;
          padding: 16px;
          text-align: center;
        }}
        header h1 {{
          margin: 0;
          font-size: 1.5em;
        }}
        header p {{
          margin: 4px 0 0;
          font-size: 0.9em;
        }}
        ul {{
          list-style: none;
          margin: 0;
          padding: 0 20px;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <header>
          <h1>Serie Fibonacci</h1>
          <p>Hora de ejecución: <em>{time_str}</em></p>
        </header>
        <ul>
          {list_items}
        </ul>
      </div>
    </body>
    </html>
    """
    return html
