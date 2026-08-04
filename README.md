# 📱 QR Code Generator using Python

A simple Python project that generates a QR code from any URL entered by the user. The generated QR code is saved as an image (`.png`) on the local computer.

## 🚀 Features

* Generate QR codes from any URL
* Save the QR code as a PNG image
* Simple and beginner-friendly Python code
* Uses the popular `qrcode` library

## 🛠️ Technologies Used

* Python 3
* qrcode
* Pillow (PIL)

## 📂 Project Structure

```
QR-Code-Generator/
│
├── qr_generator.py
├── README.md
└── qrcode.png   # Generated after running the program
```

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/QR-Code-Generator.git
```

2. Navigate to the project folder:

```bash
cd QR-Code-Generator
```

3. Install the required library:

```bash
pip install qrcode[pil]
```

## ▶️ How to Run

Run the Python file:

```bash
python qr_generator.py
```

Enter a URL when prompted:

```
Enter the URL to generate QR code:
https://github.com
```

The QR code image will be generated and saved to the specified location.

## 💻 Example Output

```
Enter the URL to generate QR code:
https://github.com

✅ QR Code generated successfully!
Saved at: C:\Users\admin\Desktop\qrcode.png
```

## 📸 Preview

After running the program, a QR code image (`qrcode.png`) will be created. Scanning the QR code opens the entered URL.

## 🔮 Future Improvements

* Add a graphical user interface (GUI) using Tkinter
* Generate QR codes for text, email, phone numbers, and Wi-Fi credentials
* Allow users to choose the save location
* Customize QR code colors and size
* Add a logo in the center of the QR code

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Srivardhan**

If you found this project helpful, consider giving it a ⭐ on GitHub!
