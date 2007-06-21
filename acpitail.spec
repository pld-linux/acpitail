# TODO: optflags; why -static?
Summary:	Shows information of an ACPI capable system
Summary(pl.UTF-8):	Wyświetlanie informacji systemu ACPI
Name:		acpitail
Version:	0.1
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://www.vanheusden.com/acpitail/%{name}-%{version}.tgz
# Source0-md5:	59b60dcdee061bc5b6a9537d269cea4b
Patch0:		%{name}-Makefile.patch
URL:		http://www.vanheusden.com/acpitail/
BuildRequires:	libacpi-devel
BuildRequires:	libacpi-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
acpitail shows information regarding the battery-state, fan-states,
temperatures, and other relevant details of an ACPI capable system
(mostly laptops).

%description -l pl.UTF-8
acpitail wyświetla informacje o stanie baterii, stanie wiatraków,
temperaturach oraz innych podobnych szczegółach systemu ACPI (głównie
w laptopach).

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_sbindir}/%{name}
