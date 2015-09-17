## -*- coding: utf-8 -*-
<html>
    <head>
        <style type="text/css">
            ${css}
            .table {
                font-size: 11px;
            }
            .table tr td {
                padding-left: 10px;

            }
            .general_info {
                width: 100%;
                font-size: 11px;
            }
            .general_info td {
                padding-left: 10px;
            }
            .code{
                font-size: 11px;
                width: 100%;
            }
            tbody tr:nth-child(2n+1) .filled{
                background-color: #E1E9F2;
            }
        </style>
    </head>
    <body>
        <p style="text-align: center; font-size:18px; border: groove lightsteelblue 1px; padding: 5px;">${_('Statistics : User by month')}</p>

        <table class="general_info">
            <tr style="color:white; background: lightsteelblue; font-size: 14px;">
                <td colspan=4>${_('General informations')}</td>
            </tr>
            <tr>
                <td>${_('User : ')}</td>
                <td>${general_info(objects[0])['user'].name}</td>
                <td>${_('Company : ')}</td>
                <td>${general_info(objects[0])['company_name']}</td>
            </tr>
            <tr>
                <td>${_('Database : ')}</td>
                <td>${general_info(objects[0])['database']}</td>
                <td>${_('Date : ')}</td>
                <td>${general_info(objects[0])['date_print']}</td>
            <tr>
        </table>
        </br></br>

        <table class="general_info">
            <tr style="color:white;background: lightsteelblue; font-size: 14px; ">
                <td style="width: 15%;">${_('Year')}</td>
                <td style="width: 25%">${_('Month')}</td>
                <td>${_('Number of active users')}</td>
            </tr>
        </table>
        <table class="general_info">
            %for year in tab_year(objects[0]) :
            <thead>
            <tr  style="font-size: 14px; ">
                <td colspan=4 style="border-bottom: solid lightsteelblue 1px;"> ${year}</td>
            </tr>
            </thead>
            <tbody>
                %for obj in objects:
                    %if obj.year == year:
                        <tr>
                            <td style="width: 15%"></td>
                            <td class="filled" style="width: 25%">${obj.month}</td>
                            <td class="filled">${obj.nb_users}</td>
                        </tr>
                    %endif
                %endfor
            </tbody>
            %endfor
        </table>


    </body>
</html>