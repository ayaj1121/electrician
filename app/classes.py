from email.mime.multipart import MIMEMultipart
from threading import Thread
from email.mime.text import MIMEText
import smtplib


class mail(Thread):
    def __init__(self,you,to,subject,user):
        print("inside constructor")
        self.you=you
        self.to=to
        self.subject=subject    
        self.user=user
        Thread.__init__(self)

    def run(self):
        # me == my email address
        # you == recipient's email address

        print("inside run")
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.you
        msg['To'] = self.to
        # html = get_template('mail_template.html').render(ctx)
  
        # print(gethtml(self.user))
        part2 = MIMEText(gethtml(self.user), 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        # msg.attach(part1)
        msg.attach(part2)

        # Send the message via local SMTP server.
        try:
            with smtplib.SMTP_SSL('heimdall.protondns.net',465) as s:
                print("ssl")
                s.login('mbelectricals@mbelectricals.in','Akhilmalik9601657865')
                s.sendmail(self.you, self.to, msg.as_string())
                s.quit()
                print("quit")
        except Exception as e:
            print(e)

        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.

def gethtml(user):
    html="""\
<!DOCTYPE HTML
	PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
	xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
	<!--[if gte mso 9]>
<xml>
	<o:OfficeDocumentSettings>
		<o:AllowPNG/>
		<o:PixelsPerInch>96</o:PixelsPerInch>
	</o:OfficeDocumentSettings>
</xml>
<![endif]-->
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="x-apple-disable-message-reformatting">
	<!--[if !mso]><!-->
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<!--<![endif]-->
	<title></title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
		integrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA=="
		crossorigin="anonymous" referrerpolicy="no-referrer" />
	<style type="text/css">
		table,
		td {
			color: #000000;
		}

		a {
			color: #0000ee;
			text-decoration: underline;
		}

		@media only screen and (min-width: 570px) {
			.u-row {
				width: 550px !important;
			}

			.u-row .u-col {
				vertical-align: top;
			}

			.u-row .u-col-100 {
				width: 550px !important;
			}

		}

		@media (max-width: 570px) {
			.u-row-container {
				max-width: 100% !important;
				padding-left: 0px !important;
				padding-right: 0px !important;
			}

			.u-row .u-col {
				min-width: 320px !important;
				max-width: 100% !important;
				display: block !important;
			}

			.u-row {
				width: calc(100% - 40px) !important;
			}

			.u-col {
				width: 100% !important;
			}

			.u-col>div {
				margin: 0 auto;
			}
		}

		body {
			margin: 0;
			padding: 0;
		}

		table,
		tr,
		td {
			vertical-align: top;
			border-collapse: collapse;
		}

		p {
			margin: 0;
		}

		.ie-container table,
		.mso-container table {
			table-layout: fixed;
		}

		* {
			line-height: inherit;
		}

		a[x-apple-data-detectors='true'] {
			color: inherit !important;
			text-decoration: none !important;
		}
	</style>



	<!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css?family=Playfair+Display:400,700&display=swap" rel="stylesheet"
		type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Raleway:400,700&display=swap" rel="stylesheet" type="text/css">
	<!--<![endif]-->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body class="clean-body u_body"
	style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #ecf0f1;color: #000000">
	<!--[if IE]><div class="ie-container"><![endif]-->
	<!--[if mso]><div class="mso-container"><![endif]-->
	<table
		style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #ecf0f1;width:100%"
		cellpadding="0" cellspacing="0">
		<tbody>
			<tr style="vertical-align: top">
				<td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
					<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #ecf0f1;"><![endif]-->


					<div class="u-row-container" style="padding: 0px;background-color: transparent">
						<div class="u-row"
							style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
							<div
								style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: transparent;"><![endif]-->

								<!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
								<div class="u-col u-col-100"
									style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
									<div style="width: 100% !important;">
										<!--[if (!mso)&(!IE)]><!-->
										<div
											style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
											<!--<![endif]-->

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:15px 10px 10px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="line-height: 140%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 140%;"><span
																		style="text-decoration: underline; font-size: 14px; line-height: 19.6px;">
																		<span
																		style="font-size: 12px; line-height: 16.8px;">
																		<a style="color:inherit;text-decoration: none;" href="www.mbelectricals.in">
																		VIEW
																			ONLINE
																		</a>
																		</span></span><span
																			style="font-size: 14px; line-height: 19.6px;"><span
																			style="font-size: 12px; line-height: 16.8px;">
																			&nbsp;</span></span>
																			
																		</span>
																</p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<!--[if (!mso)&(!IE)]><!-->
										</div>
										<!--<![endif]-->
									</div>
								</div>
								<!--[if (mso)|(IE)]></td><![endif]-->
								<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
							</div>
						</div>
					</div>



					<div class="u-row-container" style="padding: 0px;background-color: transparent">
						<div class="u-row"
							style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
							<div
								style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #ffffff;"><![endif]-->

								<!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
								<div class="u-col u-col-100"
									style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
									<div style="width: 100% !important;">
										<!--[if (!mso)&(!IE)]><!-->
										<div
											style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
											<!--<![endif]-->

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px 10px;font-family:'Raleway',sans-serif;"
															align="left">

															<table width="100%" cellpadding="0" cellspacing="0"
																border="0">
																<tr>
																	<td style="padding-right: 0px;padding-left: 0px;"
																		align="center">

																		<img align="center" border="0"
																			src="http://satkar.online/static/app/images/electrical/logo.gif"
																			alt="Logo" title="Logo"
																			style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 23%;max-width: 121.9px;"
																			width="121.9" />

																			<h1 style="color: #ff8a00;"><a style="color:inherit;text-decoration: none;" href="www.mbelectricals.in">MB Electricals</h1>
																	</td>
																</tr>
																
															</table>

														</td>
													</tr>
												</tbody>
											</table>

											<!--[if (!mso)&(!IE)]><!-->
										</div>
										<!--<![endif]-->
									</div>
								</div>
								<!--[if (mso)|(IE)]></td><![endif]-->
								<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
							</div>
						</div>
					</div>



					<div class="u-row-container" style="padding: 0px;background-color: transparent">
						<div class="u-row"
							style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
							<div
								style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #ffffff;"><![endif]-->

								<!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
								<div class="u-col u-col-100"
									style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
									<div style="width: 100% !important;">
										<!--[if (!mso)&(!IE)]><!-->
										<div
											style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
											<!--<![endif]-->

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
															align="left">

															<table height="0px" align="center" border="0"
																cellpadding="0" cellspacing="0" width="100%"
																style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px dashed #d38a0c;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
																<tbody>
																	<tr style="vertical-align: top">
																		<td
																			style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
																			<span>&#160;</span>
																		</td>
																	</tr>
																</tbody>
															</table>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:25px 10px 10px;font-family:'Raleway',sans-serif;"
															align="left">

															<h1
																style="margin: 0px; color: #d38a0c; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: 'Playfair Display',serif; font-size: 32px;">
																Appointment Scheduled at """+user.Date+"""
															</h1>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:0px 0px 10px;font-family:'Raleway',sans-serif;"
															align="left">

															<table width="100%" cellpadding="0" cellspacing="0"
																border="0">
																<tr>
																	<td style="padding-right: 0px;padding-left: 0px;"
																		align="center">

																		<img align="center" border="0"
																			src="http://satkar.online/static/app/mail_images/image-6.png"
																			alt="Money and Growth"
																			title="Money and Growth"
																			style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 100%;max-width: 550px;"
																			width="550" />

																	</td>
																</tr>
															</table>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:0px 10px 10px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="color: #2a458a; line-height: 140%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 140%;">
																	<strong><span
																			style="font-size: 20px; line-height: 28px;">Thank
																			you for Contacting MB Electricals
																			</span></strong></p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="line-height: 140%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 140%;"><span
																		style="font-size: 26px; line-height: 36.4px;">Hello """+user.First_Name+""",
																		We will contact you soon</span>
																</p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 20px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="color: #34495e; line-height: 160%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 160%;"></p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<!--[if (!mso)&(!IE)]><!-->
										</div>
										<!--<![endif]-->
									</div>
								</div>
								<!--[if (mso)|(IE)]></td><![endif]-->
								<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
							</div>
						</div>
					</div>



					<div class="u-row-container" style="padding: 0px;background-color: transparent">
						<div class="u-row"
							style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #ffffff;">
							<div
								style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #ffffff;"><![endif]-->

								<!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
								<div class="u-col u-col-100"
									style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
									<div style="width: 100% !important;">
										<!--[if (!mso)&(!IE)]><!-->
										<div
											style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
											<!--<![endif]-->

											<!-- <table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
															align="left">

															<table width="100%" cellpadding="0" cellspacing="0"
																border="0">
																<tr>
																	<td style="padding-right: 0px;padding-left: 0px;"
																		align="center">

																		<img align="center" border="0"
																			src="http://satkar.online/static/app/mail_images/image-5.png"
																			alt="Satisfaction Meter"
																			title="Satisfaction Meter"
																			style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 51%;max-width: 270.3px;"
																			width="270.3" />

																	</td>
																</tr>
															</table>

														</td>
													</tr>
												</tbody>
											</table> -->

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="line-height: 140%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 140%;">
																	<strong><span
																			style="font-size: 12px; line-height: 16.8px;">We
																			use your feedback to actively
																			improve and make sure you get the service
																			you deserve.</span></strong></p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
															align="left">

															<div align="center">
																<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;font-family:'Raleway',sans-serif;"><tr><td style="font-family:'Raleway',sans-serif;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="" style="height:40px; v-text-anchor:middle; width:224px;" arcsize="0%" stroke="f" fillcolor="#2a458a"><w:anchorlock/><center style="color:#FFFFFF;font-family:'Raleway',sans-serif;"><![endif]-->
																	<a href="tel:9601657865"
																	style="box-sizing: border-box;display: inline-block;font-family:'Raleway',sans-serif;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #2a458a; border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;">
																	<span
																		style="display:block;padding:12px 40px;line-height:120%;"><span
																			style="font-size: 14px; line-height: 16.8px;">Click to call Akhil
																			</span></span>
																</a>
																<!--[if mso]></center></v:roundrect></td></tr></table><![endif]-->
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:15px 10px 40px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="line-height: 140%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 140%;"><span
																		style="font-size: 16px; line-height: 22.4px;">Thank
																		you,</span><br /><strong><span
																			style="font-size: 12px; line-height: 16.8px;">MB Electricals</span></strong></p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<!--[if (!mso)&(!IE)]><!-->
										</div>
										<!--<![endif]-->
									</div>
								</div>
								<!--[if (mso)|(IE)]></td><![endif]-->
								<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
							</div>
						</div>
					</div>



					<div class="u-row-container" style="padding: 0px;background-color: transparent">
						<div class="u-row"
							style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
							<div
								style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: transparent;"><![endif]-->

								<!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
								<div class="u-col u-col-100"
									style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
									<div style="width: 100% !important;">
										<!--[if (!mso)&(!IE)]><!-->
										<div
											style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
											<!--<![endif]-->

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
															align="left">

															<table height="0px" align="center" border="0"
																cellpadding="0" cellspacing="0" width="100%"
																style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
																<tbody>
																	<tr style="vertical-align: top">
																		<td
																			style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
																			<span>&#160;</span>
																		</td>
																	</tr>
																</tbody>
															</table>

														</td>
													</tr>
												</tbody>
											</table>

											<!--[if (!mso)&(!IE)]><!-->
										</div>
										<!--<![endif]-->
									</div>
								</div>
								<!--[if (mso)|(IE)]></td><![endif]-->
								<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
							</div>
						</div>
					</div>



					<div class="u-row-container" style="padding: 0px;background-color: transparent">
						<div class="u-row"
							style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #2a458a;">
							<div
								style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: #2a458a;"><![endif]-->

								<!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
								<div class="u-col u-col-100"
									style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
									<div style="width: 100% !important;">
										<!--[if (!mso)&(!IE)]><!-->
										<div
											style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
											<!--<![endif]-->

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:30px 10px 10px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
															style="color: #ffffff; line-height: 140%; text-align: center; word-wrap: break-word;">
															<p style="font-size: 14px; line-height: 140%;"><span
																style="font-size: 16px; line-height: 22.4px;">
																<a style="color:inherit;text-decoration: none;" href="www.mbelectricals.in">
																	www.mbelectricals.in
																</a>
																</span>
																
															</p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
															align="left">

															<div align="center">
																<div style="display: table; max-width:155px;">
																	<!--[if (mso)|(IE)]><table width="155" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-collapse:collapse;" align="center"><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; mso-table-lspace: 0pt;mso-table-rspace: 0pt; width:155px;"><tr><![endif]-->


																	<!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 20px;" valign="top"><![endif]-->
																	<table align="left" border="0" cellspacing="0"
																		cellpadding="0" width="32" height="32"
																		style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;margin-right: 20px">
																		<tbody>
																			<tr style="vertical-align: top">
																				<td align="left" valign="middle"
																					style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
																					<a href="https://www.instagram.com/m.b_electrical_and_service/"
																						target="_blank"
																						  ><i class="fa fa-instagram" style="font-size:36px;color:#ff8a00;"></i></a>
																				</td>
																			</tr>
																		</tbody>
																	</table>
																	<!--[if (mso)|(IE)]></td><![endif]-->

																	<!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 20px;" valign="top"><![endif]-->

																	<!--[if (mso)|(IE)]></td><![endif]-->

																	<!--[if (mso)|(IE)]><td width="32" style="width:32px; padding-right: 0px;" valign="top"><![endif]-->

																	<!--[if (mso)|(IE)]></td><![endif]-->


																	<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
																</div>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="color: #ecf0f1; line-height: 140%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 140%;"><span
																		style="font-size: 12px; line-height: 16.8px;">
																	</span></p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 25px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="color: #888888; line-height: 140%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 140%;">Terms of
																	Use | Privacy Policy</p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<!--[if (!mso)&(!IE)]><!-->
										</div>
										<!--<![endif]-->
									</div>
								</div>
								<!--[if (mso)|(IE)]></td><![endif]-->
								<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
							</div>
						</div>
					</div>



					<div class="u-row-container" style="padding: 0px;background-color: transparent">
						<div class="u-row"
							style="Margin: 0 auto;min-width: 320px;max-width: 550px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
							<div
								style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
								<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:550px;"><tr style="background-color: transparent;"><![endif]-->

								<!--[if (mso)|(IE)]><td align="center" width="550" style="width: 550px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
								<div class="u-col u-col-100"
									style="max-width: 320px;min-width: 550px;display: table-cell;vertical-align: top;">
									<div style="width: 100% !important;">
										<!--[if (!mso)&(!IE)]><!-->
										<div
											style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
											<!--<![endif]-->

											<table style="font-family:'Raleway',sans-serif;" role="presentation"
												cellpadding="0" cellspacing="0" width="100%" border="0">
												<tbody>
													<tr>
														<td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 15px;font-family:'Raleway',sans-serif;"
															align="left">

															<div
																style="color: #888888; line-height: 140%; text-align: center; word-wrap: break-word;">
																<p style="font-size: 14px; line-height: 140%;">&copy;
																	2021 MB Electricals Company. All Rights Reserved.
																</p>
															</div>

														</td>
													</tr>
												</tbody>
											</table>

											<!--[if (!mso)&(!IE)]><!-->
										</div>
										<!--<![endif]-->
									</div>
								</div>
								<!--[if (mso)|(IE)]></td><![endif]-->
								<!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
							</div>
						</div>
					</div>


					<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
				</td>
			</tr>
		</tbody>
	</table>
	<!--[if mso]></div><![endif]-->
	<!--[if IE]></div><![endif]-->
</body>

</html>
    """
    return html

class adminmail(Thread):
	def __init__(self,you,to,subject,user):
		self.user=user
		self.you=you
		self.to=to
		self.subject=subject
		Thread.__init__(self)
	
	def run(self):
		print("inside run")
        # Create message container - the correct MIME type is multipart/alternative.
		msg=MIMEMultipart('alternative')
		msg['Subject']=self.subject + " for " + self.user.First_Name
		msg['From']=self.you
		msg['To']= self.to 
		html1="""\
                <html>
                <head>
				</head>
                <body>
                    <p>Hi! Akhil,<br>
                    Appointment Scheduled for """+self.user.First_Name+" "+self.user.Last_Name+"<br>Date: "+self.user.Date+"<br>Apt/Suite: "+self.user.Apt_Suite+"<br>Address: "+self.user.Address+"""
                    </p>
						<a href="tel:"""+self.user.Phone+""""
																	style="box-sizing: border-box;display: inline-block;font-family:'Raleway',sans-serif;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #2a458a; border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;">
																	<span
																		style="display:block;padding:12px 40px;line-height:120%;"><span
																			style="font-size: 14px; line-height: 16.8px;">Click to call """+self.user.First_Name+"""
																			</span></span>
																</a>
                </body>
                </html>
                """
        # # Record the MIME types of both parts - text/plain and text/html.
		part2=MIMEText(html1,'html')
        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        # msg.attach(part1)
		msg.attach(part2)
        # Send the message via local SMTP server.
		try:
			print("adminsmtp")
			with smtplib.SMTP_SSL('heimdall.protondns.net',465) as s:
				s.login('mbelectricals@mbelectricals.in','Akhilmalik9601657865')
				s.sendmail(self.you,self.to,msg.as_string())
				s.quit()
			print("adminsmtpquit")
		except Exception as e:
			print("adminmail",e)