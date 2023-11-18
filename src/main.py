import tkinter as tk
from graph_visualization import visualize_shortest_path

def visualize_path_result(start_node, end_node, hour):
    result = visualize_shortest_path(start_node, end_node, hour)

    result_window = tk.Toplevel()
    result_window.title("Resultado de la Ruta Más Corta")

    result_label = tk.Label(result_window, text=result, justify="left")
    result_label.pack()

def main():
    window = tk.Tk()
    window.title("Visualizador de Ruta Más Corta")

    start_label = tk.Label(window, text="Nodo Inicial:")
    start_entry = tk.Entry(window)
    start_label.pack()
    start_entry.pack()

    end_label = tk.Label(window, text="Nodo Final:")
    end_entry = tk.Entry(window)
    end_label.pack()
    end_entry.pack()

    hour_label = tk.Label(window, text="Hora:")
    hour_entry = tk.Entry(window)
    hour_label.pack()
    hour_entry.pack()

    def visualize_path():
        start_node = int(start_entry.get())
        end_node = int(end_entry.get())
        hour = int(hour_entry.get())
        visualize_path_result(start_node, end_node, hour)

    visualize_button = tk.Button(window, text="Visualizar Ruta", command=visualize_path)
    visualize_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
