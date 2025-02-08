import gradio as gr
import text_generator
import storage
import os
from typing import List, Optional
from handlers import list_corpora, handle_upload, generate_text, generate_text_combined, save_generated_text, open_file, delete_file, generate_text_with_word
from storage import list_saved_files

with gr.Blocks() as app:
    gr.Markdown("## Генератор на текстове с Markov Chain")
    
    with gr.Row():
        corpus_dropdown = gr.Dropdown(choices=list_corpora(), label="Избери корпус")
        file_input = gr.File(label="Качете нов файл")
        num_sentences = gr.Slider(minimum=1, maximum=10, value=5, step=1, label="Брой изречения")
    
    word_input = gr.Textbox(label="Конкретна дума (по избор)")

    generate_button = gr.Button("Генерирай текст")
    output_text = gr.Textbox(label="Генериран текст")
    generate_button.click(generate_text_combined, inputs=[corpus_dropdown, file_input, word_input, num_sentences], outputs=output_text)
    
    with gr.Row():
        filename_input = gr.Textbox(label="Име на файла (по избор)")
        save_button = gr.Button("Запази текста")
    
    save_status = gr.Textbox(label="Статус на запазване", interactive=False)
    save_button.click(save_generated_text, inputs=[output_text, filename_input], outputs=save_status)
    
    list_files_button = gr.Button("Преглед на запазени файлове")
    saved_files_output = gr.Textbox(label="Запазени файлове", interactive=False)
    list_files_button.click(list_saved_files, outputs=saved_files_output)

    with gr.Row():
        file_to_open = gr.Textbox(label="Име на файла за отваряне")
        open_file_button = gr.Button("Отвори файл")
    
    opened_file_content = gr.Textbox(label="Съдържание на файла", interactive=False)
    open_file_button.click(open_file, inputs=file_to_open, outputs=opened_file_content)

    with gr.Row():
        file_to_delete = gr.Textbox(label="Име на файла за изтриване")
        delete_file_button = gr.Button("Изтрий файл")
    
    delete_status = gr.Textbox(label="Статус на изтриване", interactive=False)
    delete_file_button.click(delete_file, inputs=file_to_delete, outputs=delete_status)

app.launch()
