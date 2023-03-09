# Program python untuk menampilkan topological sorting dari DAG
# Anita Nursi
# 21343018
# Perancangan dan Analisis Algoritma
# 202223430034

from collections import defaultdict

# Kelas yang merepresentasikan graf
class graf:
	def __init__(inti, simpul):
		inti.graf = defaultdict(list) # Kamus yang berisi adjacency List
		inti.V = simpul # Nomor dari simpul

	# fungsi untuk penambahan edge ke graf
	def tambahkanEdge(inti, u, v):
		inti.graf[u].append(v)

	# Sebuah fungsi rekursif yang digunakan untuk topologicalSort
	def topologicalSortUtil(inti, v, dikunjungi, tumpukan):

		# Tandai node terbaru sebagai dikunjungi.
		dikunjungi[v] = True

		# Ulang untuk semua simpul yang berdekatan dengan simpul ini
		for i in inti.graf[v]:
			if dikunjungi[i] == False:
				inti.topologicalSortUtil(i, dikunjungi, tumpukan)

		# Dorong simpul saat ini ke tumpukan yang menyimpan hasil
		tumpukan.append(v)

	# Fungsi untuk melakukan Topological Sort. Ini menggunakan rekursif.
	# topologicalSortUtil()
	def topologicalSort(inti):
		# Tandai semua simpul sebagai tidak dikunjungi
		dikunjungi = [False]*inti.V
		tumpukan = []

		# Panggil fungsi pembantu rekursif untuk menyimpan Topologi
		# Urutkan mulai dari semua simpul satu per satu
		for i in range(inti.V):
			if dikunjungi[i] == False:
				inti.topologicalSortUtil(i, dikunjungi, tumpukan)

		# Mencetak isi tumpukan
		print(tumpukan[::-1]) # mengembalikan daftar dalam urutan terbalik

if __name__ == '__main__':
	g = graf(6)
	g.tambahkanEdge(5, 2)
	g.tambahkanEdge(5, 0)
	g.tambahkanEdge(4, 0)
	g.tambahkanEdge(4, 1)
	g.tambahkanEdge(2, 3)
	g.tambahkanEdge(3, 1)

	print("Berikut adalah Topological Sort dari graf yang diberikan")

	# Memanggil Fungsi
	g.topologicalSort()

# Kode ini adalah kontribusi dari Neelam Yadav
