#include "cal.h"


int main (int argc, char **argv)
{
	QApplication app(argc, argv);
	Ui_Dialog widget = new Ui_Dialog;
	Ui::Dialog ui;
	ui.setupUi(widget);
	widget->show();
	return app.exec();
}
