/**
 * Created by bobo on 17.04.17.
 */



// $(document).ready(
//     function () {
//         window.setInterval(function () {
//                 // идём аджаксом на сервер, грузим данные по url, потом кладём в commentsdiv
//                 // $.ajax('http://127.0.0.1:8000/posts/1/comments/', function (data) {
//                 //     $('.commentsdiv').html(data)
//                 //
//                 // })
//                 $('.commentsdiv').load('http://127.0.0.1:8000/posts/1/comments/');
//             }, 1000
//         )
//     }
// )

// только так можно прокидывать какие-то параметры из html в js (через data-'atribute')
$(document).ready(
    function () {
        $('.commentsdiv').each(function () {
            $(this).load($(this).data('url'));

        })

        // $('#id_categories').chosen()


        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    console.log('test')
                    console.log($('meta[name=csrf]'));
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });

        // как это работает?


        $(document).on('click', 'button.ajaxlike', function () {
            var data = $(this).data();
            console.log(data);

            $.ajax({url: data.url}).done(function (data, status, response) {
                console.log(data, status, response)
            });

            // што?
            // var likesSpan = $('#likes-' + data.postid);
            // likesSpan.html("Покликали!");
            //зочем?
            return false;
        })

        $(document).on('click', 'a.updateBlogButton', function () {
            // $('fade').modal('show');
            $('#updateBlogModal').modal('show');
            // var updateBlogPlaceForForm = $('#updateblog-' + data.blogid);
            // updateBlogPlaceForForm.html("Форма работает");

        })

        // на занятии сказали, что на вновь пришедшие элементы это не повесилось
        // имеются ввиду элементы в комментариях?
        // тут просто навесили
        // $('div').click(function () {
        //     alert($(this));
        //
        // })


        // тут сложно навесили, сказав браузеру : если произошло событие клик, то пройдись по всем элементам, и для того
        // кто подходит под селектор див вызови функцию
        // $(document).on('click', 'div', function () {
        //     alert($(this));
        // })

    }
)