$(document).ready(function(){
    var countrow=0;
    var available_filter_args;
    $("#argument-select-container").hide();
    $("#argument-newvar-form-container").hide();

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    $("#add_alg_arg_popbtn").popover({
        html: true,
        animation:true,
        trigger: 'manual',
        content: function() {
            return $('#argument-newvar-form-container').html();
        }
    }).click(function(e) {
        $('.btn_pop').not(this).popover('hide');
        $(this).popover('toggle');


        $('#alg_vartype').empty();
        $('#alg_vartype').append('<option>Integer</option>');
        $('#alg_vartype').append('<option>Float</option>');
        $('#alg_vartype').append('<option>String</option>');

        $('.popover-content #alg_vartype').select2();

        var new_alg_arg_name;
        var new_alg_arg_title ;
        var new_alg_arg_type;
        var new_alg_arg_desc;
        $('.popover-content #add_new_argument_btn2').click(function (e) {
            countrow=countrow+1;
            new_alg_arg_name = $("#alg_varname").val();
            new_alg_arg_title = $("#alg_vartitle").val();
            if(check_duplicate_title_name(new_alg_arg_name,new_alg_arg_title)){
                alert("Argument name or title already exists!")
            }
            else if ((new_alg_arg_name!=null)&&(new_alg_arg_title!=null)&&(new_alg_arg_name.trim() !="")&&(new_alg_arg_title.trim()!="")){
                var edit_btn_id="edit_btn_id_" + countrow.toString();
                var del_btn_id="del_btn_id_"+ countrow.toString();
                var del_row_btn='<button type="button" id="'+del_btn_id+'"class="btn btn-primary btn-xs a-btn-slide-text">' +
                    ' <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>' +
                    '</button>';
                var edit_row_btn='<button type="button" id="'+edit_btn_id+'"class="btn btn-primary btn-xs a-btn-slide-text btn_pop">' +
                    ' <span class="glyphicon glyphicon-edit" aria-hidden="true"></span>' +
                    ' </button>';

                var edit_sel="#"+edit_btn_id;
                var del_sel="#"+del_btn_id;

                new_alg_arg_type = $("select#alg_vartype option:checked").val();
                new_alg_arg_desc = $("#alg_vardescr").val();
                var new_arg_tr_string = "<tr id='row_id_"+countrow.toString()+"'> <td>" + new_alg_arg_name + "</td> <td>" + new_alg_arg_title + "</td> <td> " + new_alg_arg_type + " </td> <td> <div style='min-width: 100%'>" + new_alg_arg_desc + " </div> </td> <td>"+ edit_row_btn +del_row_btn +" </td> </tr>";
                $('#selected-arguments-table2 tbody').append(new_arg_tr_string);

                $(edit_sel).popover({
                    html: true,
                    animation:true,
                    trigger: 'manual',
                    placement: 'left',
                    content: function() {
                        return $('#argument-newvar-form-container').html();
                    }
                }).click(function(e) {
                    $('.btn_pop').not(this).popover('hide');
                    $(this).popover('toggle');

                    $('#alg_vartype').empty();
                    $('#alg_vartype').append('<option>Integer</option>');
                    $('#alg_vartype').append('<option>Float</option>');
                    $('#alg_vartype').append('<option>String</option>');

                    $('.popover-content #alg_vartype').select2();

                    var temp="#"+$(this).attr('id');
                    temp=temp.replace("#edit_btn_id_","");
                    temp="#row_id_"+temp;

                    var temp_alg_arg_name=$(temp).children().eq(0).text();
                    var temp_alg_arg_title=$(temp).children().eq(1).text();
                    var temp_alg_arg_type=$(temp).children().eq(2).text();
                    var temp_alg_arg_desc=$(temp).children().eq(3).text();
                    $("#alg_varname").val(temp_alg_arg_name);
                    $("#alg_vartitle").val(temp_alg_arg_title);
                    $("select#alg_vartype ").val(temp_alg_arg_type.trim()).change();
                    $("#alg_vardescr").text(temp_alg_arg_desc);


                    // alert(new_alg_arg_name+" "+new_alg_arg_title+" "+new_alg_arg_type+" "+new_alg_arg_desc);
                    $('.popover-content #add_new_argument_btn2').click(function (e) {
                        new_alg_arg_name = $("#alg_varname").val();
                        new_alg_arg_title = $("#alg_vartitle").val();
                        new_alg_arg_type = $("select#alg_vartype option:checked").val();
                        new_alg_arg_desc = $("#alg_vardescr").val();
                        if ((new_alg_arg_name!=null)&&(new_alg_arg_title!=null)&&(new_alg_arg_name.trim() !="")&&(new_alg_arg_title.trim()!="")){
                            $(temp).children().eq(0).text(new_alg_arg_name);
                            $(temp).children().eq(1).text(new_alg_arg_title);
                            $(temp).children().eq(2).text(new_alg_arg_type);
                            $(temp).children().eq(3).text(new_alg_arg_desc);

                            $(edit_sel).popover("hide");
                        }else{
                            alert("Please fill the name and title of the new variable!")
                        }
                    });

                });
                $(del_sel).click(function () {
                    var temp="#"+$(this).attr('id');
                    temp=temp.replace("#del_btn_id_","");
                    temp="#row_id_"+temp;
                    $(temp).remove();

                });
                // Update service arguments on backend
                // update_service_arguments();
                //Update backend when the service is published.
                $('#add_alg_arg_popbtn').popover("hide");
            }else{
                alert("Please fill the name and title of the new variable!")
            }
        });

    });





    $("#add_filter_arg_popbtn").popover({
        html: true,
        animation:true,
        trigger: 'manual',
        content: function() {
            return $('#argument-select-container').html();
        }
    }).click(function(e) {
        $('.btn_pop').not(this).popover('hide');
        $(this).popover('toggle');


        available_filter_args = JSON.parse('{}');
        $('#selected-queries-table tbody tr').each(function( index ) {
            console.log( index + ": " + $( this ).children().eq(3).text());
            console.log( index + ": " + $( this ).children().eq(3).text().replace(/"'/g , "'").replace(/'"/g , "'").replace(/u'/g , "'").replace(/u"/g , "'").replace(/'/g , '"').replace(/False/g , '"False"').replace(/True/g , '"True"'));
            console.log( index + ": " + JSON.stringify(JSON.parse($( this ).children().eq(3).text().replace(/"'/g , "'").replace(/'"/g , "'").replace(/u'/g , "'").replace(/u"/g , "'").replace(/'/g , '"').replace(/False/g , '"False"').replace(/True/g , '"True"'))['filters']) );
            var query_doc = JSON.parse($( this ).children().eq(3).text().replace(/"'/g , "'").replace(/'"/g , "'").replace(/u'/g , "'").replace(/u"/g , "'").replace(/'/g , '"').replace(/False/g , '"False"').replace(/True/g , '"True"'));
            var filters = query_doc['filters'];
            if (filters != undefined){
                parse_filters($( this ).children().eq(0).text(), $( this ).children().eq(1).text(), filters) ;
            }
        });


        $('#query-argument-select').empty();
        $('#query-argument-select').append('<option disabled selected>-- select one of the available filters --</option>');
        // var keys = [];
        // for(var k in available_filter_args) keys.push(k);
        for(var query in available_filter_args){
            console.log(query);
            for(var arg_idx in available_filter_args[query]['filter_args']) {
                var display_name = available_filter_args[query]['display_name'];
                var arg = available_filter_args[query]['filter_args'][arg_idx];
                var arg_a = arg['a'];
                var arg_op = arg['op'];
                var arg_b = arg['b'];
                $('#query-argument-select').append('<option  data-query-id="'+query+'" data-display_name="'+display_name+'" data-arg-a="'+arg_a+'" data-arg-op="'+arg_op+'" data-arg-b="'+arg_b+'" title="' + display_name + '-' + arg_a +' '+ arg_op +' '+ arg_b + '"> ' + display_name + '-' + arg_a +' '+ arg_op +' '+ arg_b + ' </option>');
            }
        }

        $('.popover-content #query-argument-select').select2();

        var new_arg_query_id;
        var new_arg_query_display_name;
        var new_arg_a;
        var new_arg_op;
        var new_arg_b;
        var selected = false;
        $('.popover-content #query-argument-select').on('change', function() {
            selected = true;
            new_arg_query_id = $(this).children(":selected").attr("data-query-id");
            new_arg_query_display_name = $(this).children(":selected").attr("data-display_name");
            new_arg_a = $(this).children(":selected").attr("data-arg-a");
            new_arg_op = $(this).children(":selected").attr("data-arg-op");
            new_arg_b = $(this).children(":selected").attr("data-arg-b");
            $('.popover-content #filter_def_val').val(new_arg_b)
        });


        $('.popover-content #add_new_argument_btn1').click(function (e) {
            countrow=countrow+1;
            var new_filter_arg_title = $(".popover-content #filter_vartitle").val();
            var new_filter_arg_def = $(" .popover-content #filter_def_val").val();
            var new_filter_arg_desc = $(".popover-content #filter_descr").val();
            var edit_btn_id="edit_btn_id_" + countrow.toString();
            var del_btn_id="del_btn_id_"+ countrow.toString();
            var del_row_btn='<button id="' + del_btn_id +'" class="btn btn-primary btn-xs a-btn-slide-text">' +
                ' <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>' +
                '</button>';
            var edit_row_btn='<button id="'+ edit_btn_id+'" class="btn btn-primary btn-xs a-btn-slide-text btn_pop">' +
                ' <span class="glyphicon glyphicon-edit" aria-hidden="true"></span>' +
                ' </button>';
            var edit_sel="#"+edit_btn_id;
            var del_sel="#"+del_btn_id;
            if(check_duplicate_title_name("",new_filter_arg_title)){
                alert("Argument name or title already exists!")
            }
            else if((selected)&&(new_filter_arg_title!=null)&&(new_filter_arg_def!=null)&&(new_filter_arg_title.trim()!="")&&(new_filter_arg_def.trim()!="")) {
                var new_arg_tr_string = "<tr id='row_id_"+countrow.toString()+"'> <td>" + new_arg_query_id + "</td> <td>" + new_arg_query_display_name + "</td> <td> <span>" + new_arg_a + " </span><span> " + new_arg_op + "</span></td> <td> " +new_filter_arg_def + "</td> <td> " + new_filter_arg_title + "</td> <td><div  style='min-width: 100%'>" + new_filter_arg_desc + "</div></td><td>" + edit_row_btn +del_row_btn+"</td> </tr>";
                $('#selected-arguments-table1 tbody').append(new_arg_tr_string);

                $(edit_sel).popover({
                    html: true,
                    animation:true,
                    trigger: 'manual',
                    placement: 'left',
                    content: function() {
                        return $('#argument-select-container').html();
                    }
                }).click(function(e) {
                    $('.btn_pop').not(this).popover('hide');
                    $(this).popover('toggle');
                    $('.popover-content #query-argument-select').remove();

                    var temp="#"+$(this).attr('id');
                    temp=temp.replace("#edit_btn_id_","");
                    temp="#row_id_"+temp;
                    //
                    //
                    // available_filter_args = JSON.parse('{}');
                    // $('#selected-queries-table tbody tr').each(function( index ) {
                    //     console.log( index + ": " + $( this ).children().eq(3).text());
                    //     console.log( index + ": " + $( this ).children().eq(3).text().replace(/"'/g , "'").replace(/'"/g , "'").replace(/u'/g , "'").replace(/u"/g , "'").replace(/'/g , '"').replace(/False/g , '"False"').replace(/True/g , '"True"'));
                    //     console.log( index + ": " + JSON.stringify(JSON.parse($( this ).children().eq(3).text().replace(/"'/g , "'").replace(/'"/g , "'").replace(/u'/g , "'").replace(/u"/g , "'").replace(/'/g , '"').replace(/False/g , '"False"').replace(/True/g , '"True"'))['filters']) );
                    //     var query_doc = JSON.parse($( this ).children().eq(3).text().replace(/"'/g , "'").replace(/'"/g , "'").replace(/u'/g , "'").replace(/u"/g , "'").replace(/'/g , '"').replace(/False/g , '"False"').replace(/True/g , '"True"'));
                    //     var filters = query_doc['filters'];
                    //     if (filters != undefined){
                    //         parse_filters($( this ).children().eq(0).text(), $( this ).children().eq(1).text(), filters) ;
                    //     }
                    // });
                    //
                    //
                    // $('#query-argument-select').empty();
                    // for(var query in available_filter_args){
                    //     console.log(query);
                    //     for(var arg_idx in available_filter_args[query]['filter_args']) {
                    //         var display_name = available_filter_args[query]['display_name'];
                    //         var arg = available_filter_args[query]['filter_args'][arg_idx];
                    //         var arg_a = arg['a'];
                    //         var arg_op = arg['op'];
                    //         var arg_b = arg['b'];
                    //         $('#query-argument-select').append('<option  data-query-id="'+query+'" data-display_name="'+display_name+'" data-arg-a="'+arg_a+'" data-arg-op="'+arg_op+'" data-arg-b="'+arg_b+'" title="' + display_name.trim() + '-' + arg_a.trim() +' '+ arg_op.trim() +' '+ arg_b.trim() + '"> ' + display_name.trim() + '-' + arg_a.trim() +' '+ arg_op.trim() +' '+ arg_b.trim() + ' </option>');
                    //     }
                    // }
                    //
                    // $('.popover-content #query-argument-select').select2();
                    //
                    // var new_arg_query_id;
                    // var new_arg_query_display_name;
                    // var new_arg_a;
                    // var new_arg_op;
                    // var new_arg_b;
                    // var selected = false;
                    // $('.popover-content #query-argument-select').on('change', function() {
                    //     selected = true;
                    //     new_arg_query_id = $(this).children(":selected").attr("data-query-id");
                    //     new_arg_query_display_name = $(this).children(":selected").attr("data-display_name");
                    //     new_arg_a = $(this).children(":selected").attr("data-arg-a");
                    //     new_arg_op = $(this).children(":selected").attr("data-arg-op");
                    //     new_arg_b = $(this).children(":selected").attr("data-arg-b");
                    //     $('.popover-content #filter_def_val').val(new_arg_b)
                    // });

                    // var temp_query_choice=(" "+$(temp).children().eq(1).text().trim()+"-"+$(temp).children().eq(2).text().trim().replace("  "," ")+" "+$(temp).children().eq(3).text().trim()+" ");
                    var temp_filter_def_val=$(temp).children().eq(3).text();
                    var temp_filter_var_title=$(temp).children().eq(4).text();
                    var temp_filter_descr=$(temp).children().eq(5).text();


                    // $("select#select2-query-argument-select-container ").val(temp_query_choice).change();

                    $("#filter_def_val").val(temp_filter_def_val);
                    $("#filter_vartitle").val(temp_filter_var_title);
                    $("#filter_descr").text(temp_filter_descr);


                    // alert(new_alg_arg_name+" "+new_alg_arg_title+" "+new_alg_arg_type+" "+new_alg_arg_desc);
                    $('.popover-content #add_new_argument_btn1').click(function (e) {
                        var new_filter_def_val = $("#filter_def_val").val();
                        var new_filter_vartitle = $("#filter_vartitle").val();
                        var new_filter_descr =  $("#filter_descr").val();
                        if((new_filter_arg_title!=null)&&(new_filter_arg_def!=null)&&(new_filter_arg_title.trim()!="")&&(new_filter_arg_def.trim()!="")) {
                            $(temp).children().eq(3).text(new_filter_def_val);
                            $(temp).children().eq(4).text(new_filter_vartitle);
                            $(temp).children().eq(5).text(new_filter_descr);

                            $(edit_sel).popover("hide");
                        }else{
                            alert("Please fill the name and title of the new variable!")
                        }
                    });

                });
                $(del_sel).click(function () {
                    var temp="#"+$(this).attr('id');
                    temp=temp.replace("#del_btn_id_","");
                    temp="#row_id_"+temp;
                    $(temp).remove();

                });
                // Update service arguments on backend
                // update_service_arguments();
                //Chose to update arguments on backend (create JSON file) when publishing.
                selected = false;
                $('#add_filter_arg_popbtn').popover("hide");
            }
            else {
                alert("Please fill the necessary fields.")
            }

        })

    });



    function parse_filters(query_id, query_num, json){
        if(json['a'] != undefined) {
            if (json['a']['a'] == undefined) {
                if (available_filter_args[query_id] == undefined) {
                    available_filter_args[query_id] = {};
                    available_filter_args[query_id]['display_name'] = null;
                    available_filter_args[query_id]['filter_args'] = [];
                    console.log(JSON.stringify(available_filter_args));
                }
                console.log(JSON.stringify(available_filter_args));
                available_filter_args[query_id]['display_name'] = query_num;
                available_filter_args[query_id]['filter_args'].push(json);
            }
            else {
                parse_filters(query_id, query_num, json['a']);
                parse_filters(query_id, query_num, json['b']);
            }
        }
    }






    function check_duplicate_title_name(arg_name,arg_title){
        var flag=false;
        $("#selected-arguments-table1 tbody tr").each(
            function(index, elem) {
                // alert("given:"+arg_title.trim()+ " existing:"+$(this).children().eq(4).text().trim());
                if(arg_title.trim()=== $(this).children().eq(4).text().trim()) {
                    flag=true;
                }
            }
            );
        $("#selected-arguments-table2 tbody tr").each(
            function(index, elem) {
                // alert("given_name:"+arg_name.trim()+ " existing:"+$(this).children().eq(0).text().trim());
                // alert("given_title:"+arg_title.trim()+ " existing:"+$(this).children().eq(1).text().trim());
                if((arg_name.trim()=== $(this).children().eq(0).text().trim())||(arg_title.trim()=== $(this).children().eq(1).text().trim())) {
                    flag=true;
                }
            }
        );
        return flag;
    };


});


