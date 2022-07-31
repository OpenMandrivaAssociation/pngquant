Name: pngquant
Version: 2.17.0
Release: 1
Source0: https://github.com/kornelski/pngquant/archive/%{version}.tar.gz
Source1: https://github.com/ImageOptim/libimagequant/archive/a6cc4ade66710ec799ca41297f6d2c2b4070d0ff.tar.gz
Summary: PNG quantization tool for reducing image file size
URL: https://pngquant.org/
License: GPLv3+ and BSD
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(lcms2)
BuildRequires: openmp-devel

%description
pngquant converts 24/32-bit RGBA PNG images to high-quality 8-bit palette
with alpha channel preserved. Quantization significantly reduces file sizes.
Such images are fully standards-compliant and supported by all web browsers.

%prep
%autosetup -p1 -a 1
rmdir lib
mv libimagequant-* lib
# Looks a lot like autoconf but actually isn't
# Get rid of --quiet for the subdirectory so we can see errors
sed -i -e 's,--quiet,,g' configure
%configure --with-openmp

%build
%make_build

%install
%make_install

%files
%{_bindir}/pngquant
%{_mandir}/man1/pngquant.1*
