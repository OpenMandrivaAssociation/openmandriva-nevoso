%define oname Nevoso
%define bdate   2019.01.18

Summary:    Plasma 5 theme "Nevoso" for OpenMandriva
Name:   	openmandriva-nevoso
Version:    1
Release:    1
License:    GPL
Group:  Graphical desktop/KDE
Url:    https://www.opendesktop.org/u/caig/
Source0:    %{oname}%{bdate}.tar.gz

BuildRequires:	extra-cmake-modules
#BuildRequires:	cmake(ECM)
BuildArch:	noarch

%description
Nevoso Plasma 5 theme for OpenMandriva Linux

%files
%dir %{_kde5_datadir}/nevoso/themes/oma/
%{_kde5_datadir}/nevoso/themes/oma/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}

%build

%install
mkdir -p %{buildroot}%{_kde5_datadir}/nevoso/themes/oma
cp * %{buildroot}%{_kde5_datadir}/nevoso/themes/oma/

 
