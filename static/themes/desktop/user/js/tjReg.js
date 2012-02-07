// JavaScript Document
$().ready(function () {
    var reg = new regTotj();
    reg.creat();
    if ($('#workingEndedDate') && $('#workingEndedDate').hasClass('error')) {
        $('#workingEndedDate').parent().find('.tipicon').removeClass('cueRight valiOk').addClass('info');
    }
    $('#regImproveForm').bind('blur', function () {
        if ($('#workingEndedDate') && $('#workingEndedDate').hasClass('error')) {
            $('#workingEndedDate').parent().find('.tipicon').removeClass('cueRight valiOk').addClass('info');
        }
    });
})
var dateReg = new Date().getFullYear();
var regTotj;
regTotj = function () {
    var p = this;
    this.breakEmailCheck = false;//验证email
    this.successEmail = "";		//验证email
    this.regRules;
    this.regLang = {
        regLangZh:{
            wrongCue:{
                "name":"请正确填写您的真实姓名.",
                "comname":"请正确填写您的公司名称.",
                "faren":"请正确填写您的法人姓名.",
                "certify":"请正确填写您的法人身份证号码.",
                "jigou":"请正确填写您的组织机构代码证号码.",
                "szd":"请正确填写您的公司注册所在地.",
            },
            commenCue:{
                "name":"请填写您的真实中文姓名.",
                "comname":"请填写您的公司名称.",
                "faren":"请填写您的法人姓名.",
                "certify":"请填写法人身份证号码.",
                "jigou":"请填写您的组织机构代码证号码.",
                "szd":"请填写您的公司注册所在地.",
            }
        },
        regLangChoosed:{}
    };
    this.creat = function () {
        this.setLang();
        this.jobChange();
        this.validataEx();
        this.regRules = $("#regImproveForm").validate({
            event:"keyup",
            ignore:".ignore",
            onkeyup:false,
            onclick:false,
            focusInvalid:true,
            debug:false,
            rules:{
                "name":{
                    required:true,
                    minlength:2,
                    maxlength:20,
                    nameSafeCheck:true
                },
                "comname":{
                    required:true,
                    minlength:2,
                    maxlength:80,
                    nameSafeCheck:true
                },
                "faren":{
                    required:true,
                    minlength:2,
                    maxlength:12,
                    nameSafeCheck:true
                },
                "certify":{
                    required:true,
                    minlength:2,
                    maxlength:80,
                    nameSafeCheck:true
                },
                "jigou":{
                    required:true,
                    minlength:2,
                    maxlength:36,
                    nameSafeCheck:true
                },
                "szd":{
                    required:true,
                    minlength:2,
                    maxlength:80,
                    nameSafeCheck:true
                }


            },
            messages:p.regLang.regLangChoosed.wrongCue,
            success:function (label) {
                label.parent().parent().prev().find(".tipicon").removeClass("info").addClass("cueRight valiOK");
            },
            errorPlacement:function (error, element) {
                element.parent().find(".tipicon").removeClass("cueRight valiOK").addClass("info");
                var child = element.parent().next().children();
                child.html("");
                error.appendTo(child);
            },
            submitHandler:function (form) {
                $("#proceed").attr('disabled', 'disabled');
                form.submit();
            }

        })
        this.valiFocus();
        this.valiBlur();
        this.initTimeQueenCheck();
        this.studyTimeCheck();

    }
    this.setLang = function () {
        var lang = $("#tjreg").attr("language");
        if (lang == "en_US") {
            this.regLang.regLangChoosed = this.regLang.regLangEn;
        } else {
            this.regLang.regLangChoosed = this.regLang.regLangZh;
        }
    }
    this.valiFocus = function () {
        $(".protocal-info dd input").bind("focus", function () {
            if (!$(this).parent().find(".tipicon").hasClass("cueRight")) {
                p.showCom(this)
            }
        })
    }
    this.valiBlur = function () {
        $(".protocal-info dd input ").bind("blur", function () {
            //p.hideRight();
            //if(!$(this).val()){
            //	p.showWrong(this)
            //}
            if ($(this).val() == "") {
                $(this).parent().find(".tipicon").removeClass("cueRight valiOK").addClass("cueCommen");
                return;
            }
            if ($(this).hasClass("error")) {
                $(this).parent().find(".tipicon").removeClass("cueRight valiOK").addClass("info");
            } else {
                $(this).parent().find(".tipicon").removeClass("info").addClass("cueRight valiOK");
            }
        })
        $(".slt1").bind("change", function () {
            var a = !$(".slt1")[0].selectedIndex < 1;
            if (a) {
                $(this).parent().find(".tipicon").removeClass("cueRight valiOK").addClass("info");
            } else {
                $(this).parent().find(".tipicon").removeClass("info").addClass("cueRight valiOK");
            }
        })
    }
    this.showCom = function (obj) {
        var objName = $(obj).attr("name");
        $(obj).parent().next().children().html(p.regLang.regLangChoosed.commenCue[objName]);
        $(obj).parent().find(".tipicon").removeClass("cueRight valiOK info").addClass("cueCommen");
    }
    this.showWrong = function (obj) {
        var objName = $(obj).attr("name");
        if (typeof(p.regLang.regLangChoosed.wrongCue[objName]) == "object") {
            $(obj).parent().find(".tipicon").removeClass("cueRight valiOK cueCommen").addClass("info");
            $(obj).parent().next().children().html(p.regLang.regLangChoosed.wrongCue[objName].def);
        } else {
            $(obj).parent().find(".tipicon").removeClass("cueRight valiOK cueCommen").addClass("info");
            $(obj).parent().next().children().html(p.regLang.regLangChoosed.wrongCue[objName]);
        }
    }
    this.hideRight = function (obj) {
        $(obj).parent().find(".tipicon").removeClass("cueRight valiOK cueCommen");
    }
    this.validataEx = function () {
        this.proStatusCheck();
        this.visibleCheck();
        // this.emailUsedCheck();
        this.nameSafeCheck();
        this.enameSafeCheck();
        this.fieldCheck();
        //this.functionCheck();
        this.workDateCheck();
        this.workDateNopassCheck();
        this.emailSoonCheck();
        this.requiredOrNot();
        this.dataRequired();
        this.limitMinYear();
        this.limitMaxYear();
        this.selectchangefix();
        this.jobChange();
        this.functionChange();
    }
    this.nameSafeCheck = function () {
        jQuery.validator.addMethod("nameSafeCheck", function (value, element) {
            var aa = $(element).attr("value");
            var testRule = aa.match(/^([\u4e00-\u9fa5]|[a-zA-Z]|[\(\)\-\_\·]){2,20}$/ig) ? true : false;
            return testRule;
        }, "");
    }
    this.enameSafeCheck = function () {
        jQuery.validator.addMethod("enameSafeCheck", function (value, element) {
            var aa = $(element).attr("value");
            var testRule = aa.match(/^([a-zA-Z]|[\(\)\-\_\·]){2,20}$/ig) ? true : false;
            return testRule;
        }, "");
    }
    this.emailSoonCheck = function () {                               //validate email is valid or not
        jQuery.validator.addMethod("emailSoonCheck", function (value, element) {
            var email = $(element).attr("value");
            if (p.successEmail && p.successEmail == $(element).attr("value")) {
                return true;
            }
            if (p.breakEmailCheck == true) {
                return false
            }
            else {
                $.ajax({
                    url:"#" + $("#email").attr("value"),
                    dataType:"jsonp",
                    success:function (data) {
                        if (data.flag == false) {
                            $(element).next().removeClass("info").addClass("cueRight").html("&nbsp;");
                            for (i = 0; i < p.regRules.errorList.length; i++) {
                                if (p.regRules.errorList[i].element == element) {
                                    p.regRules.errorList.slice(i, 1)
                                }
                            }
                            p.successEmail = email;
                            $("#emailerror").html("");
                            $(element).removeClass("error").addClass("valid").blur();
                        } else {
                            $("#emailerror").html(p.regRules.settings.messages.field = p.regLang.regLangChoosed.wrongCue.emailBeReg);
                        }
                        p.breakEmailCheck = false;
                    }
                })
            }
            p.breakEmailCheck = true;
        }, "");
    }
    this.jobChange = function () {
        var sel = $("select#jobStatus");
        sel.bind("change", function () {
            if ($("select#jobStatus")[0].selectedIndex == "0") {
                sel.next().removeClass("cueRight valiOK").addClass("info");
            }
        })
    }
    this.functionChange = function () {
        var fc = $("#function");
        fc.bind("change", function () {
            if ($("#function").val() == "36") {
                $("#otherFunction").css("display", "inline");
                $("#otherFunction").next().removeClass("cueRight valiOK").addClass("info");
            } else {
                $("#otherFunction").css("display", "none");
            }
        })
    }
    this.visibleCheck = function () {
        jQuery.validator.addMethod("visible", function (value, element) {
            var a = !$("#country")[0].selectedIndex < 1;
            var b = !$("#province")[0].selectedIndex < 1 || !$("#province:visible");
            var c = !$("#city")[0].selectedIndex < 1 || !$("#city:visible");
            return a && b && c;
        }, "");
    }
    this.selectchangefix = function () {
        var a = !$("#country").length < 1;
        var b = !$("#province").length < 1;
        if (a) {
            $("#country").bind("change", function () {
                $("#country").parent().find(".tipicon").removeClass("cueRight valiOK").addClass("info");
            })
        } else {
            return;
        }
        if (b) {
            $("#province").bind("change", function () {
                $("#province").parent().find(".tipicon").removeClass("cueRight valiOK").addClass("info");
            })
        } else {
            return;
        }
    }
    this.fieldCheck = function () {
        jQuery.validator.addMethod("fieldCheck", function (value, element) {
            var a = !$("#industry")[0].selectedIndex < 1;
            var b = !$("#subIndustry")[0].selectedIndex < 1 || $("#subIndustry")[0].style.display == "none";
            var c = !$("#otherIndustry").attr("value") == "" || $("#otherIndustry")[0].style.display == "none" ? true : false;
            return a && b && c;
        }, "");
    }
    this.workDateNopassCheck = function () {
        jQuery.validator.addMethod("workDateNopassCheck", function (value, element) {
            var parent = $(element).parent().parent();
            var selectList = parent.find("input");
            var a = $(selectList[0]).val();
            var b = $(selectList[1]).val();
            var d;
            if (a && b) {
                d = b >= a ? true : false
            } else if (!a && !b) {
                d = true
            } else {
                d = false
            }
            return d;
        }, "");

    }
    this.requiredOrNot = function () {
        jQuery.validator.addMethod("requiredOrNot", function (value, element) {
            if ($(element).hasClass("requiredTrue")) {
                if (!$(element).val()) {
                    return false;
                } else {
                    return true
                }
            } else {
                return true;
            }
        }, "");
    }
    this.initTimeQueenCheck = function () {
        $(".present").bind("click", function () {
            function focusandblur(obj) {
                obj.focus();
                obj.blur();
            }

            var startDate = $("#workingStartedDate");
            var endedDate = $("#workingEndedDate");
            // if(this.checked==true){
            // endedDate.attr("readonly","readonly");
            endedDate.val(dateReg);
            // endedDate.addClass('ignore');
            // if($("#workingStartedDate").val()!=""){
            // $("#workingStartedDate").addClass("ignore");
            // }
            // if(startDate.val()==""){
            // elementName = startDate.attr("name");
            // startDate.parent().find(".tipicon").addClass("info").remove("cueRight cueCommen");
            // startDate.parent().next().children().html(p.regLang.regLangChoosed.commenCue[elementName]);
            // startDate.focus();
            // }else if(endedDate.prev().prev().val()&&endedDate.prev().prev().val()>=1950&&endedDate.prev().prev().val()<=dateReg){
            // endedDate.parent().find(".tipicon").addClass("cueRight").remove("info cueCommen");
            // focusandblur(startDate);
            // }else{
            // var elementName = startDate.attr("name");
            // endedDate.parent().find(".tipicon").addClass("info").remove("cueRight cueCommen");
            // endedDate.parent().next().children().html(p.regLang.regLangChoosed.commenCue[elementName]);
            // focusandblur(startDate);
            // }
            // }else{
            // endedDate.removeAttr("readonly").removeClass('ignore');
            // endedDate.val("");
            // focusandblur(startDate);
            // focusandblur(endedDate);
            // if($("#workingStartedDate").addClass("ignore")){$("#workingStartedDate").removeClass("ignore");}
            // }
            if (this.checked == true) {
                endedDate.attr("readonly", "readonly");
                endedDate.val(dateReg);

                if (startDate.val() == "") {
                    elementName = startDate.attr("name");
                    startDate.parent().find(".tipicon").addClass("info").remove("cueRight cueCommen");
                    startDate.parent().next().children().html(p.regLang.regLangChoosed.commenCue[elementName]);
                    startDate.focus();
                } else if (endedDate.prev().prev().val() && endedDate.prev().prev().val() >= 1950 && endedDate.prev().prev().val() <= dateReg) {
                    endedDate.parent().find(".tipicon").addClass("cueRight").remove("info cueCommen");
                    focusandblur(startDate);
                } else {
                    var elementName = startDate.attr("name");
                    endedDate.parent().find(".tipicon").addClass("info").remove("cueRight cueCommen");
                    endedDate.parent().next().children().html(p.regLang.regLangChoosed.commenCue[elementName]);
                    focusandblur(startDate);
                }
            } else {
                endedDate.removeAttr("readonly")
                endedDate.val("");
                focusandblur(startDate);
                focusandblur(endedDate);
            }
        })
        $("#workingEndedDate").blur(function () {
            $("#workingStartedDate").focus();
            $("#workingStartedDate").blur();
        });
    }

    this.workDateCheck = function () {
        jQuery.validator.addMethod("workDateCheck", function (value, element) {
            var a = $("#workingStartedDate").val();
            var b = $("#workingEndedDate").val();
            return a && b || !a && !b;
        }, "");
    }
    this.dataRequired = function () {
        jQuery.validator.addMethod("dataRequired", function (value, element) {
            var a = $("#studyingStartedDate").val();
            var b = $("#studyingEndedDate").val();
            if (a != "" | b != "") {

                return a && b;
            } else {
                return true;
            }
        }, "");
    }
    this.limitMinYear = function () {
        jQuery.validator.addMethod("limitMinYear", function (value, element) {
            if ($(element).val() && $(element).val() < 1950) {
                return false;
            } else {
                return true;
            }
        }, "");
    }
    this.limitMaxYear = function () {
        jQuery.validator.addMethod("limitMaxYear", function (value, element) {
            if ($(element).val() && $(element).val() > dateReg) {
                return false;
            } else {
                return true;
            }
        }, "");
    }
    this.proStatusCheck = function () {
        jQuery.validator.addMethod("proStatusRequired", function (value, element) {
            var c = value == "" ? false : true;
            return c;
        }, "");
    }
    this.functionCheck = function () {
        jQuery.validator.addMethod("functionCheck", function (value, element) {
            if ($(element).hasClass("requiredTrue")) {
                var a = $("#function").val() >= 1 && $("#function").val() != 36;
                var b = $("#function").val() == 36 && $("#otherFunction").val() != "";
                return a || b;
            } else {
                return true;
            }
        }, "");
    }
    this.studyTimeCheck = function () {
        var lab = $("#studyingEndedDate").parent().next().find(".regcue");
        if (lab.hasClass("error")) {
            $("#studyingEndedDate").next().addClass("info").remove("cueRight cueCommen");
        }
    }
};