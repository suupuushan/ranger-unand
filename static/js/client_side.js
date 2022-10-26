$(document).ready(function(){
    
    // -[Prediksi Model]---------------------------
    // Fungsi untuk memanggil API ketika tombol prediksi ditekan
    // id button: prediksi_submit_dt, prediksi_submit_knn, prediksi_submit_kmeans, prediksi_submit_nb
    $("#prediksi_rf").click(function(e) {
      e.preventDefault();
      modelType = "Random Forest"   
      sendData(modelType); 
    })
  
    $("#prediksi_gaussian").click(function(e) {
      e.preventDefault();   
      modelType = "GaussianNB"   
      sendData(modelType); 
    })
  
    $("#prediksi_knn").click(function(e) {
      e.preventDefault();   
      modelType = "KNN"   
      sendData(modelType); 
    })
  
    $("#prediksi_svm").click(function(e) {
      e.preventDefault();   
      modelType = "SVM"   
      sendData(modelType); 
    })
  
    function sendData(modelType){
      // Set data pengukuran bunga iris dari input pengguna
      var input_sepal_length = $("#range_sepal_length").val(); 
      var input_sepal_width  = $("#range_sepal_width").val(); 
      var input_petal_length = $("#range_petal_length").val(); 
      var input_petal_width  = $("#range_petal_width").val(); 
  
      // Panggil API dengan timeout 1 detik (1000 ms)
      setTimeout(function() {
      try {
        $.ajax({
          url  : "/api/deteksi",
          type : "POST",
          data : {"sepal_length" : input_sepal_length,
              "sepal_width"  : input_sepal_width,
              "petal_length" : input_petal_length,
              "petal_width"  : input_petal_width,
              "modelType"    : modelType,
                 },
          success:function(res){
          // Ambil hasil prediksi spesies dan path gambar spesies dari API
          res_data_prediksi   = res['prediksi']
          res_gambar_prediksi = res['gambar_prediksi']
          
          // Tampilkan hasil prediksi ke halaman web
          generate_prediksi(res_data_prediksi, res_gambar_prediksi); 
          }
        });
      }
      catch(e) {
        // Jika gagal memanggil API, tampilkan error di console
        console.log("Gagal !");
        console.log(e);
      } 
      }, 1000)
    }

    // Fungsi untuk menampilkan hasil prediksi model
    function generate_prediksi(data_prediksi, image_prediksi) {
      var str="";
      str += "<h5 class='mb-4' style='color: #4797ff; font-family: Poppins; font-weight: 400;'>Hasil Prediksi " + modelType + "</h5>";
      str += "<br>";
      str += "<img src='" + image_prediksi + "' width=\"300\" height=\"225\"></img>"
      str += "<h3>" + data_prediksi + "</h3>";
      $("#hasil_prediksi").html(str);
    }  
    
  })
    
  