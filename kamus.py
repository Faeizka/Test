meme_dict = {
            "Cringe": "Sesuatu yang sangat aneh atau memalukan",
            "Lol": "Tanggapan umum terhadap sesuatu yang lucu",
            "Skibidi": "Sesuatu tanggapan terhadap hal yang aneh atau lucu",
            "Sigma": "Sesuatu saat dimana seseorang merasa keren",
            "Brainrot": "Sesuatu gejala dimana seseorang terlalu terobsesi kepada konten berkualitas rendah secara berlebihan"
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Opss, kata tidak ditemukan, cobalah kata lain")
