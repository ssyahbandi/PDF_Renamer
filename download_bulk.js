const buttons = document.querySelectorAll('#DownloadButton');
let delay = 2000; // 2000 mili detik atau 2 detik, ubah bila perlu.

buttons.forEach((button, index) => {
  setTimeout(() => {
    if (button && button.click) {
      try {
        button.click();
        console.log(`PDF ${index + 1} telah terunduh.`);
      } catch (error) {
        console.error(`Gagal mengunduh PDF ${index + 1}:`, error);
      }
    } else {
      console.warn(`Tombol dengan indeks ${index} tidak dapat diklik.`);
    }
  }, delay * index);
});
