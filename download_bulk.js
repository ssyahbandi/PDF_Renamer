//script by Channel XMedia (Recode By Syahbandi)

javascript:(function() {
    // Fungsi untuk menunggu elemen muncul di DOM
    function waitForElement(selector, timeout = 5000) {
        return new Promise((resolve, reject) => {
            const start = Date.now();
            
            (function check() {
                const element = document.querySelector(selector);
                if (element) {
                    resolve(element);
                } else if (Date.now() - start >= timeout) {
                    reject(new Error("Timeout: Tombol download tidak ditemukan, pastikan Faktur sudah Approved"));
                } else {
                    requestAnimationFrame(check);
                }
            })();
        });
    }

    // Fungsi utama untuk mendownload semua PDF
    async function downloadAllPDFs() {
        try {
            // Tunggu tombol download muncul dengan timeout 10 detik
            await waitForElement("#DownloadButton", 10000);
            
            // Ambil semua tombol download
            const buttons = document.querySelectorAll("#DownloadButton");
            
            if (buttons.length === 0) {
                throw new Error("No download buttons found");
            }

            // Klik setiap tombol yang terlihat
            buttons.forEach(button => {
                if (button && button.offsetParent !== null) {
                    button.click();
                }
            });

            // Tampilkan pesan sukses setelah 2 detik
            setTimeout(() => {
                alert("Download selesai");
            }, 2000);

        } catch (error) {
            console.error("Error saat Download:", error);
            alert("Error: " + error.message);
        }
    }

    // Jalankan fungsi utama
    downloadAllPDFs();
})();
