###  Генерация матрицы инцидентности комплекса Вьеториса — Рипса по точкам
Скрипт generate_vr_boundary_matrix.py читает облако точек,
генерирует по нему комплекса Вьеториса — Рипса, сохраняет его матрицу инцидентности в двух форматах.

Он принимает следующие аргументы:
- pointcloud_name - название облака точек в папке datasets/pointclouds (без расширения)
- max_edge_length - диаметр комплекса Вьеториса — Рипса
- max_dimension - размерность, вплоть до которой будут генерироваться симплексы 

В результате в папку datasets/vr_boundary_matrices будут сохранены два файла с матрицами: один в формате, который понимает PHAT, другой в формате, который понимает MetalTopology.

Пример запуска:
```
python3 generate_vr_boundary_matrix.py -p human_gene -e 35 -d 2
```